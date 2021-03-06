import os
_Base_Dir = os.path.basename(os.path.dirname(__file__)) + '/'

Source = [ ('moex/' + x) for x in [
    'ALRS', 'GAZP', 'GMKN', 'LKOH', 'MGNT', 'MOEX', 'ROSN', 'SBER', 'SBERP', 'VTBR',
    'USDRUB_TOD', 'Brent',
    'MICEX10'
]]

Default_Timezone = 'Europe/Moscow'

Work_Date = ['2018-07-01', '2019-04-02']
Work_Time = ['10:01', '18:40']

Dataset_File = _Base_Dir + 'dataset.csv.gz'

Input_Size = len(Source) - 1
