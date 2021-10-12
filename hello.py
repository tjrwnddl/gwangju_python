import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 늘하던거라... 뭐 괜찮지 않아?
print("helloworld 헬로 월드")
print("hello")
print("hello2")