/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */



var compactObject = function(obj) {
    if (Array.isArray(obj)) {
        let returnArray = [];
        for (let item of obj) {
            if (Boolean(item)) {
                let subObject;
                if (typeof item === "object") {
                    subObject = compactObject(item)
                } else {
                    subObject = item;
                }
                returnArray.push(subObject)
            }
        }
        return returnArray;
        
    } else if (typeof obj === "object") {
        let returnObject = {};
        for (let objKey of Object.keys(obj)) {
            let item = obj[objKey];
            if (Boolean(item)) {
                let subObject;
                if (typeof item === "object") {
                    subObject = compactObject(item)
                } else {
                    subObject = item;
                }
                returnObject[objKey] = subObject;
            }
        }
        return returnObject;
    }


    
};