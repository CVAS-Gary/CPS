from src.cache import get_from_cache, set_to_cache

class UserService:
    def __init__(self):
        self.users = [
            {"id": "u1", "active": True, "tier": "free"},
            {"id": "u2", "active": True, "tier": "pro"},
            {"id": "u3", "active": False, "tier": "pro"},
        ]

    def get_users(self):
        return self.users

    def get_active_users_by_tier(self, tier: str):
        # 先檢查快取
        cache_key = f"users.active.{tier}"
        cached = get_from_cache(cache_key)
        if cached:
            print("Telemetry: users.active.fetch (cache hit)")
            return cached

        # 過濾 active 且符合 tier 的使用者
        result = [u for u in self.users if u["active"] and u["tier"] == tier]

        # 存到快取
        set_to_cache(cache_key, result)

        # Telemetry 模擬
        print("Telemetry: users.active.fetch (cache miss)")

        return result