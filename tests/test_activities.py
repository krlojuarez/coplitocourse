"""
Tests for the /activities endpoint (GET activities list)
"""

from fastapi.testclient import TestClient
from src.app import app


def test_get_activities_returns_all_activities():
    """Test that GET /activities returns all 9 activities with correct structure"""
    client = TestClient(app)
    response = client.get("/activities")
    
    assert response.status_code == 200
    activities = response.json()
    
    # Verify we have all 9 activities
    assert len(activities) == 9
    
    # Verify the expected activity names exist
    expected_activities = [
        "Chess Club",
        "Programming Class",
        "Gym Class",
        "Basketball Team",
        "Soccer Club",
        "Art Club",
        "Drama Club",
        "Debate Club",
        "Science Club"
    ]
    for activity_name in expected_activities:
        assert activity_name in activities
    
    # Verify each activity has the correct structure
    for activity_name, activity_data in activities.items():
        assert "description" in activity_data
        assert "schedule" in activity_data
        assert "max_participants" in activity_data
        assert "participants" in activity_data
        assert isinstance(activity_data["description"], str)
        assert isinstance(activity_data["schedule"], str)
        assert isinstance(activity_data["max_participants"], int)
        assert isinstance(activity_data["participants"], list)
