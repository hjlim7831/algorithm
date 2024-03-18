/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    let joinedDict = {};
    for (let item of arr1) {
        joinedDict[item["id"]] = item
    }
    
    for (let item of arr2) {
        let id = item["id"];
        if (id in joinedDict) {
            for (let field of Object.keys(item)) {
                joinedDict[id][field] = item[field]
            }
        } else {
            joinedDict[id] = item        
        }
    }
    
    let joinedArray = [];
    
    for (let itemKey of Object.keys(joinedDict)) {
        joinedArray.push(joinedDict[itemKey]);
    }
    
    return joinedArray;
    
};