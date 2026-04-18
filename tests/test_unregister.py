"""
Tests for the /activities/{activity_name}/unregister endpoint (DELETE unregister)
"""

from fastapi.testclient import TestClient
from src.app import app


def test_unregister_from_activity_success():
    """Test that a student can successfully unregister from an activity"""
    client = TestClient(app)
    
    # First, sign up for an activity
    activity_name = "Soccer Club"
    email = "student@mergington.edu"
    
    # Sign up first
    signup_response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )
    assert signup_response.status_code == 200
    
    # Verify student was added
    activities_before = client.get("/activities").json()
    assert email in activities_before[activity_name]["participants"]
    
    # Now unregister
    unregister_response = client.delete(
        f"/activities/{activity_name}/unregister",
        params={"email": email}
    )
    
    # Verify success response
    assert unregister_response.status_code == 200
    data = unregister_response.json()
    assert "message" in data
    assert email in data["message"]
    assert activity_name in data["message"]
    
    # Verify the participant was actually removed
    activities_after = client.get("/activities").json()
    assert email not in activities_after[activity_name]["participants"]
