from typing import Any, Dict
from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError
import logging
import requests

class TelegraphProvider(ToolProvider):
    def _validate_credentials(self, credentials: Dict[str, Any]) -> None:
        access_token = credentials.get("telegraph_access_token")
        if not access_token:
            raise ToolProviderCredentialValidationError("Telegraph Access Token 不能为空。")

        try:
            logging.info("直接用 requests 验证 Telegraph Access Token。")
            url = "https://api.telegra.ph/getAccountInfo"
            params = {
                "access_token": access_token
            }
            response = requests.get(url, params=params, timeout=10)
            data = response.json()
            logging.debug(f"账号信息响应: {data}")

            if not data.get("ok"):
                error_description = data.get("error", "Unknown error")
                raise ToolProviderCredentialValidationError(f"API 返回非OK状态: {error_description}")

            logging.info("Telegraph Access Token 验证成功。")

        except Exception as e:
            logging.exception("Telegraph 凭证验证失败。")
            raise ToolProviderCredentialValidationError(f"Telegraph 凭证验证遇到意外错误: {str(e)}")
