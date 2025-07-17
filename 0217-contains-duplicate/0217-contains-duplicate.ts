function containsDuplicate(nums: number[]): boolean {
    let mySet: Set<number> = new Set<number>(nums);

    return (mySet.size < nums.length)

};