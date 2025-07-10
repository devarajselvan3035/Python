<<<<<<< HEAD

caption = "   "

r, f = 0, 0
ans = '#'
while r < len(caption):
    if caption[r] == ' ':
        f = 1
    elif f == 1 and caption[r].isalpha():
        ans += caption[r].upper()
        f = 0
        pass
    elif r == 0 or f == 0:
        ans += caption[r].lower()
    r += 1
print(ans[:100])
=======
nums = [1,2,2,1,1,0]

i = 1
while i < len(nums):
    if nums[i-1] == nums[i]:
        nums[i] = 0
        nums[i-1] = nums[i-1] * 2
        i += 1
    i +=1

l, r = 0, 0
while r < len(nums):
    if nums[r] != 0:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
    r += 1
print(nums)


>>>>>>> 4fb318a (python-10/07/2025)
