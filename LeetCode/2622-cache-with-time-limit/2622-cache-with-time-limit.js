var TimeLimitedCache = function() {
    this.customCache = {};
    this.timeoutIds = {};
    
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    const keyExists = key in this.customCache;
    if (keyExists) {
        clearTimeout(this.timeoutIds[key]);
    }
    
    this.customCache[key] = value
    
    const timeoutId = setTimeout(() => {
        delete this.customCache[key]
    }, duration)
    
    this.timeoutIds[key] = timeoutId
    
    return keyExists;
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    if (key in this.customCache) {
        return this.customCache[key];
    } else {
        return -1;
    }
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    return Object.keys(this.customCache).length;
    
};

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */