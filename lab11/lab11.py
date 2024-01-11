import pandas as pd
from Bio.Cluster import kcluster


def load_expression_data():
    yeast_expression_file_name = 'yeast_expression.txt'
    df = pd.read_csv(yeast_expression_file_name, sep='\t')

    return df


def cluster_data(df: pd.DataFrame):
    yeast_df = df.copy()

    yeast_df = yeast_df.drop(columns=['GENE'])

    mask = yeast_df.map(lambda val: 0 if val == 'x' else 1).values

    yeast_df = yeast_df.map(lambda val: 0 if val == 'x' else float(val))

    yeast_matrix = yeast_df.values

    cluster_id, _, _ = kcluster(data=yeast_matrix, nclusters=2, mask=mask, transpose=True)

    return cluster_id


if __name__ == '__main__':
    df = load_expression_data()
    cluster_id = cluster_data(df)

    print(cluster_id)
