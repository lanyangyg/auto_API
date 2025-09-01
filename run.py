import os
import subprocess
import sys
from pathlib import Path


def ensure_directories():
    """确保必要的目录存在"""
    directories = ["allure-results", "allure-report"]
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✓ 确保目录存在: {directory}")


def run_tests():
    """运行测试"""
    print("🔄 开始运行测试...")
    try:
        # 构建命令
        cmd = [
            sys.executable, "-m", "pytest",
            "test_cases",  # 指定测试目录
            "--alluredir=allure-results",  # 指定allure结果目录
            "--clean-alluredir",  # 清理旧结果
            "-v"  # 详细输出
        ]

        # 执行命令
        result = subprocess.run(cmd)

        if result.returncode == 0:
            print("✅ 测试运行成功")
            return True
        else:
            print("❌ 测试运行失败")
            return False
    except Exception as e:
        print(f"❌ 运行测试时出错: {e}")
        return False


def generate_allure_report():
    """生成Allure报告"""
    print("📊 生成Allure报告...")
    try:
        # 检查allure命令是否存在
        subprocess.run(["allure", "--version"],
                       capture_output=True, check=True)

        # 生成报告
        cmd = [
            "allure", "generate",
            "allure-results",
            "--clean",
            "-o", "allure-report"
        ]

        result = subprocess.run(cmd)

        if result.returncode == 0:
            print("✅ Allure报告生成成功")
            return True
        else:
            print("❌ Allure报告生成失败")
            return False

    except subprocess.CalledProcessError:
        print("❌ 未找到allure命令，请确保已安装allure-commandline")
        print("   安装方式:")
        print("   - macOS: brew install allure")
        print("   - Windows: 下载并安装allure-commandline")
        print("   - Ubuntu: sudo apt install allure")
        return False
    except Exception as e:
        print(f"❌ 生成Allure报告时出错: {e}")
        return False


# def open_report():
#     """打开报告"""
#     report_path = Path("allure-report") / "index.html"
#     if report_path.exists():
#         print(f"📂 报告路径: {report_path.absolute()}")
#         try:
#             if sys.platform == "darwin":  # macOS
#                 subprocess.run(["open", str(report_path)])
#             elif sys.platform == "win32":  # Windows
#                 subprocess.run(["start", str(report_path)], shell=True)
#             else:  # Linux
#                 subprocess.run(["xdg-open", str(report_path)])
#             print("🌐 已在浏览器中打开Allure报告")
#         except Exception as e:
#             print(f"⚠️  无法自动打开报告: {e}")
#             print(f"💡 请手动打开: {report_path.absolute()}")
#     else:
#         print("❌ 报告文件不存在")


def main():
    """主函数"""
    print("🚀 API测试执行器")
    print("=" * 50)

    # 确保目录存在
    ensure_directories()

    # 运行测试
    if not run_tests():
        print("❌ 测试失败，停止执行")
        return 1

    # 生成报告
    if not generate_allure_report():
        print("❌ 报告生成失败")
        return 1

    # 打开报告
    # open_report()

    print("=" * 50)
    print("🎉 测试和报告生成完成")
    return 0


if __name__ == "__main__":
    sys.exit(main())
