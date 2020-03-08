
import re
from datetime import datetime


class DateFormatHelper(object):
    regex1 = re.compile(r"[0-9]{1,2}-[0-9]{1,2} *[A-Za-z]+ *[0-9]{4}")
    regex2 = re.compile(r"[0-9]{1,2} *[A-Za-z]+ *[0-9]{4}")
    regex3 = re.compile(r"[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}")
    regex4 = re.compile(r"[A-Za-z]+ *[0-9]{1,2}, *[0-9]{4}")
    regex5 = re.compile(r"[A-Za-z]+ *[0-9]{1,2}-[0-9]{1,2}, *[0-9]{4}")
    regex6 = re.compile(r"[0-9]{4}年[0-9]{1,2}月[0-9]{1,2}日")
    dateformatregexs = [regex1, regex2, regex3, regex4, regex5, regex6]

    monthMap = {"sep": "9", "oct": "10", "nov": "11", "dec": "12", "jan": "1", "feb": "2",
                "aug": "8", "jul": "7", "jun": "6", "may": "5", "apr": "4", "mar": "3"}
    monthMap2 = {"September": "9", "October": "10", "November": "11", "December": "12",
                 "January": "1", "February": "2", "August": "8", "July": "7",
                 "June": "6", "May": "5", "April": "4", "March": "3"}

    @classmethod
    def convertStandardDateFormat(cls, datestr: str) -> str:
        """
        轉換日期格式
        :param datestr:
        :return:
        """
        res = ""
        if datestr is None:
            return res
        for i in range(0, len(cls.dateformatregexs)):
            try:
                regex = cls.dateformatregexs[i]
                match = regex.match(datestr)
                if match is not None:
                    itemstr = match.group()
                    if i == 0:
                        items = str(itemstr).split(" ")
                        year = items[len(items) - 1]
                        month = cls.monthMap.get(str(items[1]).lower())
                        if month is None:
                            month = cls.monthMap2.get(str(items[1]))
                        dayrange = str(items[0])
                        day = dayrange[0:dayrange.index("-")]
                        day2 = dayrange[dayrange.index("-") + 1:]
                        res = year + "-" + month + "-" + day
                        # res2 = year + "-" + month + "-" + str(day2)
                    elif i == 1:
                        items = str(itemstr).split(" ")
                        year = items[len(items) - 1]
                        month = cls.monthMap.get(str(items[1]).lower())
                        if month is None:
                            month = cls.monthMap2.get(str(items[1]))
                        day = items[0]
                        res = year + "-" + month + "-" + day
                    elif i == 3:
                        items = str(itemstr).split(" ")
                        year = items[len(items) - 1]
                        month = cls.monthMap.get(str(items[0]).lower())
                        if month is None:
                            month = cls.monthMap2.get(str(items[0]))
                        digit_pattern = re.compile(r'[0-9]+')
                        digitlist = digit_pattern.findall(items[1])
                        day = digitlist[0]
                        res = year + "-" + month + "-" + day
                    elif i == 4:
                        items = str(itemstr).split(" ")
                        year = items[len(items) - 1]
                        month = cls.monthMap.get(str(items[0]).lower())
                        if month is None:
                            month = cls.monthMap2.get(str(items[0]))
                        dayrange = str(items[1])
                        day = dayrange[0:dayrange.index("-")]
                        # day2 = dayrange[dayrange.index("-")+1:dayrange.index(",")]
                        res = year + "-" + month + "-" + day
                        # res2 = year + "-" + month + "-" + day2
                    elif i == 5:
                        for x in range(len(str(itemstr))):
                            if ord(itemstr[x]) > 255:
                                itemstr = itemstr.replace(itemstr[x], " ")
                        items = str(itemstr).split(" ")
                        year = items[0]
                        month = items[1]
                        day = items[2]
                        res = year + "-" + month + "-" + day
                    else:
                        res = datestr
                    break
            except Exception as e:
                print("convertStandardDateFormat方法出現異常{}".format(e))
        return datetime.strptime(res, '%Y-%m-%d')
