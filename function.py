import keyboard
import time

# Block all keys (iterating through standard key scan codes)
for i in range(150):
    keyboard.block_key(i)

print("Keyboard locked for 5 seconds...")
time.sleep(5)

# Unblock all keys
for i in range(150):
    keyboard.unblock_key(i)
print("Keyboard unlocked.")
