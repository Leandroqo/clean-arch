from src.adapter.http_adapter import HttpAdapterInterface
import httpx


class HttpX(HttpAdapterInterface):
	def _get(url: str) -> dict:
		r = httpx.get(url)
		return r.json()