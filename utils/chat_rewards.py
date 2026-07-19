import random
import time

from utils.storage import get_user, update_user

CHAT_REWARD_MIN = 5
CHAT_REWARD_MAX = 15
CHAT_REWARD_COOLDOWN = 300  # 5 minutes


async def try_chat_reward(message):
    """Reward active chatters with Nyxium."""

    profile = get_user(message.author.name)

    current_time = int(time.time())
    last_reward = profile.get("last_chat_reward", 0)

    if current_time - last_reward < CHAT_REWARD_COOLDOWN:
        return

    reward = random.randint(CHAT_REWARD_MIN, CHAT_REWARD_MAX)

    profile["nyxium"] += reward
    profile["last_chat_reward"] = current_time

    update_user(message.author.name, profile)