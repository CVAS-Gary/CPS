'''
任務：請在 src/user_service.py 擴充 UserService，新增方法 get_active_users_by_tier(tier: str)。
限制：
- 使用 src/cache.py 快取，鍵名 'users.active.{tier}'
- Telemetry：用 print() 模擬，命名 'users.active.fetch'
- 不修改 get_users()，避免 N+1 Query
驗收：tests/test_user_service.py 測試通過
'''
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
        cache_key = f'users.active.{tier}'
        cached_result = get_from_cache(cache_key)
        if cached_result is not None:
            return cached_result

        print('Telemetry: users.active.fetch')
        result = [user for user in self.users if user['active'] and user['tier'] == tier]
        set_to_cache(cache_key, result)
        return result