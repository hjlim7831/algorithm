/**
 * @param {number[]} nums
 * @return {void}
 */
var ArrayWrapper = function(nums) {
    this.item = nums;
    
};

/**
 * @return {number}
 */
ArrayWrapper.prototype.valueOf = function() {
    if (this.item.length === 0) {
        return 0;
    } else {
        return this.item.reduce((total, current) => {
            return total + current;
        })        
    }
    
}

/**
 * @return {string}
 */
ArrayWrapper.prototype.toString = function() {
    return `[${this.item.join(",")}]`
    
    
}

/**
 * const obj1 = new ArrayWrapper([1,2]);
 * const obj2 = new ArrayWrapper([3,4]);
 * obj1 + obj2; // 10
 * String(obj1); // "[1,2]"
 * String(obj2); // "[3,4]"
 */