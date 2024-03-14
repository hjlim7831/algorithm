/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    let chunkedArray = [];
    
    for (let i = 0; i < arr.length / size; i++) {
         const stIdx = i * size
         const edIdx = Math.min((i + 1) * size, arr.length)
         
         chunkedArray.push(arr.slice(stIdx, edIdx))         
     }
    return chunkedArray;
    
};
