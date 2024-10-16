from pathlib import Path

import nonebot
from pydantic import BaseModel

from .utils import ConfigsManager


class BotSetting(BaseModel):
    self_nickname: str = ""
    """回复时NICKNAME"""
    system_proxy: str | None = None
    """系统代理"""
    db_url: str = ""
    """数据库链接"""
    platform_superusers: dict[str, list[str]] = {}
    """平台超级用户"""

    def get_superuser(self, platform: str) -> list[str]:
        """获取超级用户

        参数:
            platform: 对应平台

        返回:
            list[str]: 超级用户id
        """
        if self.platform_superusers:
            return self.platform_superusers.get(platform, [])
        return []

    def get_sql_type(self) -> str:
        """获取数据库类型

        返回:
            str: 数据库类型, postgres, aiomysql, sqlite
        """
        return self.db_url.split(":", 1)[0] if self.db_url else ""


Config = ConfigsManager(Path() / "data" / "configs" / "plugins2config.yaml")

BotConfig = nonebot.get_plugin_config(BotSetting)