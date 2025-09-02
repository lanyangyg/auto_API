import logging
import colorlog

def setup_logger():
    """
    配置并返回一个全局的、带颜色的日志记录器（logger）。
    这个函数的核心是防止重复配置和重复添加处理器（handler），
    确保在整个项目中调用它时，都返回同一个配置好的logger实例。
    """
    # 1. 使用一个固定的名称来获取logger实例。只要名称相同，获取到的就是同一个实例。
    logger = logging.getLogger("api_automation_logger")
    logger.setLevel(logging.INFO)

    # 2. 检查这个logger是否已经有了处理器，如果没有，才进行配置。
    #    这是为了防止在多个模块中导入并调用此函数时，重复添加处理器导致日志输出多次。
    if not logger.handlers:
        # 创建一个控制台处理器 (Handler)
        handler = colorlog.StreamHandler()

        # 创建一个带颜色的格式器 (Formatter)
        formatter = colorlog.ColoredFormatter(
            '%(log_color)s%(asctime)s - %(levelname)s - %(message)s',
            log_colors={
                'DEBUG':    'cyan',
                'INFO':     'green',
                'WARNING':  'yellow',
                'ERROR':    'red',
                'CRITICAL': 'red,bg_white',
            },
            reset=True,
            style='%'
        )

        # 3. 将格式器添加到处理器，再将处理器添加到logger中
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    # 4. 返回配置好的logger实例
    return logger

# 创建一个全局可用的logger实例，项目中其他模块可以直接导入这个log变量使用
log = setup_logger()