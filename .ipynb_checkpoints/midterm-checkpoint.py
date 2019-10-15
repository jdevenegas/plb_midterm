import pandas as pd

def import_data():
    '''

    Please make sure the files are in the directory that we are running the
    Python code.

    The difference between these two files, they are counted from different
    directions thus they will have different index. Each row is one leaf, for
    each leaf we have 21 data points to outline the shape of the leaf. Each
    point we have x-coordinates and y-coordinates. So we have 21x2 data
    points for each leaf. These are x and y coordinates are our features.

    '''
    # Other data
    #Allometry_Tips_Data = 'Allometry_tips.csv'
    #Allometry_Base_Data = 'Allometry_base.csv'

    # Data We Will Use
    Procrustes_Base_Data = 'Procrustes_base.csv'
    Procrustes_Tips_Data = 'Procrustes_tips.csv'

    # Base:
    Procrustes_Base_Data = pd.read_csv(
        Procrustes_Base_Data,
        header='infer')


    Procrustes_Tips_Data = pd.read_csv(
        Procrustes_Tips_Data,
        header='infer')


    data_list = [Procrustes_Base_Data, Procrustes_Tips_Data]
    return data_list

def get_nulls(my_df):
    null_columns = my_df.columns[my_df.isnull().any()]
    count_of_null = my_df[null_columns].isnull().sum()
    print('Counts of null values per column: ' '\n', count_of_null, '\n')
    rows_where_null = my_df[my_df.isnull().any(axis=1)][null_columns].head()
    print('Rows where null exist: ', '\n', rows_where_null, '\n')



data_list = import_data()
Procrustes_Base_Data = data_list[0]
Procrustes_Tips_Data = data_list[1]
print(Procrustes_Tips_Data.head())
