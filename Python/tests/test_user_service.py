from src.user_service import UserService

def test_get_active_users_by_tier():
    svc = UserService()

    # 第一次呼叫 → cache miss
    result1 = svc.get_active_users_by_tier("pro")
    assert all(u["active"] for u in result1)
    assert all(u["tier"] == "pro" for u in result1)

    # 第二次呼叫 → cache hit
    result2 = svc.get_active_users_by_tier("pro")
    assert result1 == result2