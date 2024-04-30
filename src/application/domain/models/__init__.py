from .auth_model import AuthModel
from .aluno_model import CreateAlunoModel, AlunoModel, AlunoList, AlunoQueryModel
from .professor_model import (
    CreateProfessorModel,
    ProfessorModel,
    ProfessorList,
    ProfessorQueryModel,
)
from .credential_model import (
    CredentialModel,
    RefreshCredentialModel,
    ResetCredentialModel,
)
from .solicitacao_model import (
    CreateSolicitacaoModel,
    UpdateSolicitacaoModel,
    SolicitacaoModel,
    SolicitacaoList,
    SolicitacaoQueryModel,
)
from .orientacao_model import (
    CreateOrientacaoModel,
    UpdateOrientacaoModel,
    OrientacaoModel,
    OrientacaoList,
    OrientacaoQueryModel,
)
from .banca_model import BancaModel, BancaList, BancaQueryModel
