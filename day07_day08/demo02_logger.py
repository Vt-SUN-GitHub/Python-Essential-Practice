import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.Logger(__name__)

logger.debug('调试日志')
logger.error('系统故障')

