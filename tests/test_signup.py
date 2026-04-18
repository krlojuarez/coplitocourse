"""
Tests for the /activities/{activity_name}/signup endpoint (POST signup)
"""

from fastapi.testclient import TestClient
from src.app import app


def test_signup_for_activity_success():
    """Test that a student can successfully sign up for an activity"""
    client = TestClient(app)
    
    # Pick an activity with no initial participants (Basketball Team)
    activity_name = "Basketball Team"
    email = "newstudent@mergington.edu"
    
    # Send signup request
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )
    
    # Verify success response
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert email in data["message"]
    assert activity_name in data["message"]
    
    # Verify the participant was actually added
    activities_response = client.get("/activities")
    activities = activities_response.json()
    assert email in activities[activity_name]["participants"]
