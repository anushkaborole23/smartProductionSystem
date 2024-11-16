from users.models import AssetLayerModel,UserIntegrationLayerModel,UserCommunicationLayerModel,UserInformationLayerModel,UserFunctionalLayerModel,UserBusinessLayerModel
from django_pandas.io import read_frame
class AdminPCAAlgorithm:
    def preProcessPCA(self):
        d1 = AssetLayerModel.objects.all()
        d2 = UserIntegrationLayerModel.objects.all()
        d3 = UserCommunicationLayerModel.objects.all()
        d4 = UserInformationLayerModel.objects.all()
        d5 = UserFunctionalLayerModel.objects.all()
        d6 = UserBusinessLayerModel.objects.all()
        d1 = read_frame(d1)
        d2 = read_frame(d2)
        d3 = read_frame(d3)
        d4 = read_frame(d4)
        d5 = read_frame(d5)
        d6 = read_frame(d6)
        import pandas as pd
        d4['schemaregistry'] = d4['schemaregistry'].replace(['NaN','True','False'],['0','1','0'])
        d4['da'] = d4['da'].replace(['NaN','True', 'False'], ['0','1', '0'])
        frames = [d1, d2, d3, d4, d5, d6]
        df = pd.concat(frames)
        print(df.dtypes)
        df = df[['shift', 'productquantity', 'noofworkers', 'filesize', 'humanmachineinterface', 'plcslaves']]
        df = df.fillna(df.mean())
        print(df.head())
        from sklearn.decomposition import PCA
        pca = PCA(n_components=2)
        pca.fit(df)
        variance = pca.explained_variance_ratio_
        singular = pca.singular_values_

        import numpy as np
        import matplotlib
        import matplotlib.pyplot as plt

        # Make a random array and then make it positive-definite
        num_vars = df.shape[0]
        num_obs = df.shape[1]
        A = np.random.randn(num_obs, num_vars)
        A = np.asmatrix(A.T) * np.asmatrix(A)
        U, S, V = np.linalg.svd(A)
        eigvals = S ** 2 / np.sum(S ** 2)  # NOTE (@amoeba): These are not PCA eigenvalues.
        # This question is about SVD.

        fig = plt.figure(figsize=(8, 5))
        sing_vals = np.arange(num_vars) + 1
        plt.plot(sing_vals, eigvals, 'ro-', linewidth=2)
        plt.title('PCA Model Building')
        plt.xlabel('Principal Component')
        plt.ylabel('Eigenvalue')
        # I don't like the default legend so I typically make mine like below, e.g.
        # with smaller fonts and a bit transparent so I do not cover up data, and make
        # it moveable by the viewer in case upper-right is a bad place for it
        leg = plt.legend(['Eigenvalues from SVD'], loc='best', borderpad=0.3,
                         shadow=False, prop=matplotlib.font_manager.FontProperties(size='small'),
                         markerscale=0.4)
        leg.get_frame().set_alpha(0.4)
        # leg.draggable(state=True)
        plt.show()

        return df,variance, singular






