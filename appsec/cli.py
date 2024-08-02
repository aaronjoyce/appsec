import asyncio
import argparse

from .appsec import main


def cli():
    parser = argparse.ArgumentParser(prog="appsec", description="AppSec PR requestor")
    parser.add_argument('--repo', help='The GitHub repo to which the commit(s) belong')
    parser.add_argument('--from', help='The source commit SHA or tag to compare from')
    parser.add_argument('--to', help='The target commit SHA or tag to compare against')

    args = parser.parse_args()
    print(("args", args))

    asyncio.run(
        main(
            api_token="",
        )
    )





