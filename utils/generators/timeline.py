from utils.general_utils import int_to_string as its, CustomError
from typing import Optional, Tuple, List


DAY30MONTHS = (4, 6, 9, 11)


class TimelineGenerator:

    @staticmethod
    def generate_datetime_string(
        year: int,
        month: Optional[int]=None, 
        day: Optional[int]=None, 
        hour: Optional[int]=None) -> str:
        # 2020-01-01 00:00:00 EST
        
        if month is not None:
            if month < 1 or month > 12:
                raise CustomError("Generating datetime string with INVALID MONTH.")
            if day is not None:
                if day < 1 or (month == 2 and day > 28) or (month in DAY30MONTHS and day > 30) or day > 31:
                    raise CustomError("Generating datetime string with INVALID DAY.")
                if hour is not None:
                    if hour < 0 or hour > 24:
                        raise CustomError("Generating datetime string with INVALID HOUR.")
                    return f"{year}-{its(month)}-{its(day)} {its(hour)}:00:00 EST"
                return f"{year}-{its(month)}-{its(day)}"
            return f"{year}-{its(month)}"
        return f"{year}"

    @staticmethod
    def generate_timeline(
        _year: Tuple[int, ...]=(2018,),     # Default: The year of 2018
        _month: Tuple[int, ...]=(1,),       # Default: Months from 1 to 12
        _day: Tuple[int, ...]=(1,),         # Default: Days from 1 to 31 (if possible)
        _hour: Tuple[int, ...]=(8,16),      # Default: Hours from 08:00 to 16:00
        target: str='day') -> List[List[str]]:
        
        timeline = []
        for year in range(_year[0], _year[1] + 1 if len(_year) == 2 else _year[0] + 1):
            if target == 'year':
                timeline.append([TimelineGenerator.generate_datetime_string(year)])
            else:
                for month in range(_month[0], _month[1] + 1 if len(_month) == 2 else 13):
                    if target == 'month':
                        timeline.append([TimelineGenerator.generate_datetime_string(year, month)])
                    else:
                        for day in range(_day[0], _day[1] + 1 if len(_day) == 2 else 32):
                            if (month == 2 and day > 28) or (month in DAY30MONTHS and day > 30):
                                continue
                            if target == 'day':
                                timeline.append([TimelineGenerator.generate_datetime_string(year, month, day)])
                            else:
                                for hour in range(_hour[0], _hour[1] + 1 if len(_hour) == 2 else 24):
                                    if target == 'hour':
                                        timeline.append([TimelineGenerator.generate_datetime_string(year, month, day, hour)])
        return timeline
