class EventEmitter {
    constructor() {
        this.events = {};
    }
    
    /**
     * @param {string} eventName
     * @param {Function} callback
     * @return {Object}
     */
    subscribe(eventName, callback) {
        if (!(eventName in this.events)) {
            this.events[eventName] = [];
        }
        this.events[eventName].push(callback)
        
        return {
            unsubscribe: () => {
                this.events[eventName] = this.events[eventName].filter(item => item !== callback);      
            }
        };
    }
    
    /**
     * @param {string} eventName
     * @param {Array} args
     * @return {Array}
     */
    emit(eventName, args = []) {
        let returnArray = [];
        if (this.events[eventName]) {
            for (let callbackFn of this.events[eventName]) {
                
                returnArray.push(callbackFn(...args));
            }
            
        }
        return returnArray;
    }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */