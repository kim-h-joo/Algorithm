while(1):
    nums = list(map(int, input().split()))
    if nums == [0,0,0]:
        exit()
    nums.sort()
    if (nums[0]**2 + nums[1]**2 == nums[2]**2):
        print("right")
    else:
        print("wrong")
        