class Solution:
    def reformatDate(self, date: str) -> str:
        months = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}

        yy = date[-4:]
        i = 1
        for i in range(len(date)):
            if not date[i].isnumeric():
                break

        dd = date[:i]
        if len(dd) == 1:
            dd = '0' + dd
        mm = months[date[-8:-5]]
        return f'{yy}-{mm}-{dd}'


Solution().reformatDate(date = "20th Oct 2052")
