import logging
import sys
from tenacity import retry, stop, wait, wait_fixed, \
    wait_random, stop_after_attempt, stop_after_delay,\
    wait_exponential, before_log

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)

# def random_failure():
#     r = random.randint(0, 100)
#     if r > 50:
#         print(r)
#         raise IOError("Broken, failed")
#     else:
#         return "All done!"
#
# @retry
# def never_give_up_never_surrender():
#     print("Retry forever ignoring Exceptions, don't wait between retries")
#     raise Exception
#
#
# @retry(stop=stop_after_attempt(7))
# def stop_after_7_attempts():
#     print("Stopping after 7 attempts")
#     raise Exception
#
#
# @retry(stop=stop_after_delay(10))
# def stop_after_10_s():
#     print("Stopping after 10 seconds")
#     raise Exception
#
#
# @retry(stop=(stop_after_delay(10) | stop_after_attempt(5)))
# def stop_after_10_s_or_5_retries():
#     print("Stopping after 10 seconds or 5 retries")
#     raise Exception
#
#
# @retry(wait=wait_fixed(2))
# def wait_2_s():
#     print("Wait 2 second between retries")
#     raise Exception
#
#
# @retry(reraise=True, stop=stop_after_attempt(4), wait=wait_exponential(multiplier=1, min=4, max=10))
# def wait_exponential_1():
#     print("Wait 2^x * 1 sec between each retry starting with 4 sec, then up to 10 sec, then 10 sec afterwards")
#     raise Exception
#
#
# @retry(reraise=True, stop=stop_after_attempt(4), wait=wait_random(min=1, max=2))
# def raise_my_exception():
#     raise Exception("Fail")
#


@retry(reraise=True,
       stop=stop_after_attempt(4),
       wait=wait_random(min=1, max=2),
       before=before_log(LOGGER, logging.DEBUG))
def wait_random_1_to_2_s():
    raise Exception


if __name__ == '__main__':
    try:
        wait_random_1_to_2_s()
    except Exception:
        pass
    print(wait_random_1_to_2_s.retry.statistics)
