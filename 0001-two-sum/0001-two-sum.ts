function twoSum(nums: number[], target: number): number[] {
    const answer: { [key: number]: number } = {};

    for (let i = 0; i < nums.length; i++) {
        answer[nums[i]] = i;
    }

    for (let j = 0; j < nums.length; j++) {
        const comp = target - nums[j];
        if (comp in answer && answer[comp] !== j) {
            return [j, answer[comp]];
        }
    }

    return null;
};