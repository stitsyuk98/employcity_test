import pandas as pd


def cut_chunck(df, chunk_size):
    res_list = [pd.DataFrame()]
    #df.sort_values(by='dt', inplace=True)
    for key in df['dt'].unique():
        print(key)
        if res_list[-1].shape[0] >= chunk_size:
            print('add new df, because last batch has len ', res_list[-1].shape[0])
            res_list.append(pd.DataFrame())
        res_list[-1] = pd.concat([res_list[-1], df[df['dt'] == key]])
        print('add rows, ', 'result ', res_list)
    return res_list


if __name__ == '__main__':

    dfs = pd.date_range(
        "2023-01-01 00:00:00", 
        "2023-01-01 00:00:05", 
        freq="s"
    )
    df1 = pd.DataFrame({"dt": dfs.repeat(2)})

    dfs = pd.date_range(
        "2023-01-01 00:00:03", 
        "2023-01-01 00:00:07", 
        freq="s"
    )
    df2 = pd.DataFrame({"dt": dfs.repeat(1)})

    df = pd.concat([df1, df2])

    # print(df.head(10))
    # print(df['dt'].head(10))
    # print(df.info())
    # print(df.shape)

    print(df.groupby('dt')['dt'].count())
    # print(type(df['dt'].astype(str).unique().tolist()))

    cut_chunck(df, 5)