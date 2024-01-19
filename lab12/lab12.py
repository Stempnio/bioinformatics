import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def read_aminoacid_properties() -> (pd.DataFrame, pd.Series):
    aminoacid_properties_file_name = 'aaProperties.txt'

    df = pd.read_csv(aminoacid_properties_file_name, sep=';', header=None)
    aminoacid_names = df.iloc[:, 0]
    df = df.drop(columns=[0])
    df = df.replace(',', '.', regex=True)
    df = df.astype(float)

    return df, aminoacid_names


def normalize_df(df: pd.DataFrame) -> pd.DataFrame:
    return df.apply(lambda col: (col - np.mean(col)) / np.std(col))


def calculate_covariance_matrix(df: pd.DataFrame) -> pd.DataFrame:
    return df.cov()


def calculate_eig(cov_matrix: pd.DataFrame) -> (np.ndarray, np.ndarray):
    return np.linalg.eig(cov_matrix)


def sort_eig(eigenvalues: np.ndarray, eigenvectors: np.ndarray) -> (np.ndarray, np.ndarray):
    sorted_index = np.argsort(eigenvalues)[::-1]
    sorted_eigenvalues = eigenvalues[sorted_index]
    sorted_eigenvectors = eigenvectors[:, sorted_index]

    return sorted_eigenvalues, sorted_eigenvectors


def select_top_2_eigenvectors(sorted_eigenvectors: np.ndarray) -> (np.ndarray, np.ndarray):
    pc1 = sorted_eigenvectors[:, 0]
    pc2 = sorted_eigenvectors[:, 1]

    return pc1, pc2


def project_data(df: pd.DataFrame, pc1: np.ndarray, pc2: np.ndarray) -> pd.DataFrame:
    return df.dot(np.column_stack((pc1, pc2)))


def calculate_variance_explained(eigenvalues: np.ndarray) -> (float, float):
    total_variance = sum(eigenvalues)
    variance_explained_pc1 = eigenvalues[0] / total_variance
    variance_explained_pc2 = eigenvalues[1] / total_variance

    return variance_explained_pc1, variance_explained_pc2


def plot_data(transformed_data: pd.DataFrame, aminoacid_names: pd.Series):
    plt.figure(figsize=(10, 6))

    variance_explained_pc1, variance_explained_pc2 = calculate_variance_explained(eigenvalues)

    plt.xlabel(f'PC1 ({variance_explained_pc1 * 100:.2f}% of variance)')
    plt.ylabel(f'PC2 ({variance_explained_pc2 * 100:.2f}% of variance)')

    for i, txt in enumerate(aminoacid_names):
        plt.scatter(transformed_data.iloc[i, 0], transformed_data.iloc[i, 1], alpha=0.8)
        plt.text(transformed_data.iloc[i, 0], transformed_data.iloc[i, 1], txt, fontsize=9)

    plt.grid()
    plt.show()


if __name__ == '__main__':
    df, aminoacid_names = read_aminoacid_properties()
    normalized_df = normalize_df(df)
    covariance_matrix = calculate_covariance_matrix(normalized_df)
    eigenvalues, eigenvectors = calculate_eig(covariance_matrix)
    sorted_eigenvalues, sorted_eigenvectors = sort_eig(eigenvalues, eigenvectors)
    pc1, pc2 = select_top_2_eigenvectors(sorted_eigenvectors)
    print('PC1:', pc1)
    print('PC2:', pc2)
    transformed_data = project_data(normalized_df, pc1, pc2)
    plot_data(transformed_data, aminoacid_names)
    print('Aminokwasy znajdujące się blisko siebie na wykresie mają podobne właściwości.')
    print('Przykładowo')
    print(' - aminokwasy F,L oraz I są umieszczone blisko siebie, co wskazuje na podobieństwo właściwości.')
    print(' - aminokwasy R i C są od siebie bardzo odległe, może odzwierciedlać ich odmienne właściwości.')
