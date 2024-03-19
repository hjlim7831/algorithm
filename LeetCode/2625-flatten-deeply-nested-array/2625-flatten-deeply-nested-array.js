/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */

let getFlatten = function(arr, d, n) {
    if (d == n) {
        return arr;
    }
    let returnArray = [];
    for (let item of arr) {
        if (Array.isArray(item)) {
            let midArr = getFlatten(item, d+1, n)
            returnArray.push(...midArr);
        } else {
            returnArray.push(item)
        }
    }
    return returnArray;
}

var flat = function (arr, n) {    
    return getFlatten(arr, 0, n);
};