function twoSum(nums: number[], target: number): number[] {

    const dictionary: {[key: number]:number} = {};

    for (let i = 0; i < nums.length; i++){
        dictionary[nums[i]] = i;
    }

    for (let j = 0; j < nums.length; j++){
        const comp = target - nums[j];

        if (comp in dictionary && dictionary[comp] !== j){
            return [j, dictionary[comp]]
        }
    }
    return null
    
    };
