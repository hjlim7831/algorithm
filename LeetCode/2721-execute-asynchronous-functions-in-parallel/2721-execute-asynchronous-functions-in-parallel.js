/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    return new Promise((resolve, reject) => {
        const results = [];
        let completedCount = 0;
        let rejected = false;
        
        functions.forEach((func, index) => {
            func().then(
            (result) => {
                if (!rejected) {
                    results[index] = result;
                    completedCount++;
                    if (completedCount === functions.length) {
                        resolve(results);
                    }
                }
            },
            (reason) => {
                if (!rejected) {
                    rejected = true;
                    reject(reason);
                }
            })
        })
    })
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */