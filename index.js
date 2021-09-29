// Convert to Number to Tone marks 
// Arrange in Traditional, Simplified and Pinyin (Tone Marks)
// These file will be used in merge.py
// Change number in HSK1 to 1,2,3,4,5,6,7-9

var PinyinConverter = require('./pinyin_converter.js')

var args = process.argv.slice(2);

var pinyin = PinyinConverter.convert(args[0]);
console.log(pinyin)