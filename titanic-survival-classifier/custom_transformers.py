from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.impute import KNNImputer
import numpy as np
import pandas as pd

class CustomStringImputer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass 
        
    def fit(self, X, y = None):
        return self
    
    def transform(self, X, y = None):
        X_transformed = X.copy()
        for col in X_transformed.select_dtypes(exclude=["float64", "int64"]).columns:
            X_transformed.loc[:,col] = X.loc[:,col].fillna("N/A")

        return X_transformed


class CustomKNNImputer(KNNImputer):
    def __init__(self,
                 missing_values=np.nan,
                 n_neighbors=3,
                 weights="uniform",
                 metric="nan_euclidean"):

        super().__init__(missing_values=missing_values,
                         n_neighbors=n_neighbors,
                         weights=weights,
                         metric=metric)
        
    def fit(self, X, y = None):
        X_num = X.select_dtypes(include=["float64", "int64"])
        super().fit(X_num)
        return self
    
    def transform(self, X, y = None):
        X_num = X.select_dtypes(include=["float64", "int64"])
        X_num_transformed = super().transform(X_num)
        X_transformed = pd.concat([
                            pd.DataFrame(X_num_transformed,
                                             columns=X.select_dtypes(include=["float64", "int64"]).columns).reset_index(drop=True),
                                         X.select_dtypes(exclude=["float64", "int64"]).reset_index(drop=True)], axis=1)
        return X_transformed