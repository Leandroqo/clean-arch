from abc import ABCMeta, abstractmethod


class HttpAdapterInterface(metaclass=ABCMeta):
	@abstractmethod
	def _get(self, url: str) -> dict:
		raise NotImplementedError