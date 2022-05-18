import pytest
import torch

from chrispnet.modules.encoder.conformer_encoder import ConformerEncoder


@pytest.mark.parametrize("input_size", [80])
@pytest.mark.parametrize("n_layers", [1, 2])
@pytest.mark.parametrize("d_model", [256])
@pytest.mark.parametrize("feat_out", [-1])
@pytest.mark.parametrize("subsampling", ["striding", "vggnet"])
@pytest.mark.parametrize("subsampling_factor", [4, 8])
@pytest.mark.parametrize("subsampling_conv_channels", [-1])
@pytest.mark.parametrize("ff_expansion_factor", [4])
@pytest.mark.parametrize("self_attention_model", ["rel_pos"])
@pytest.mark.parametrize("n_heads", [4])
@pytest.mark.parametrize("att_context_size", [[-1, -1], [5, 0]])
@pytest.mark.parametrize("conv_kernel_size", [31, 7])
@pytest.mark.parametrize("conv_norm_type", ["batch_norm", "layer_norm"])
def test_Encoder_forward_backward(
    input_size,
    n_layers,
    d_model,
    feat_out,
    subsampling,
    subsampling_factor,
    subsampling_conv_channels,
    ff_expansion_factor,
    self_attention_model,
    n_heads,
    att_context_size,
    conv_kernel_size,
    conv_norm_type,
):

    encoder = ConformerEncoder(
        feat_in=input_size,
        n_layers=n_layers,
        d_model=d_model,
        feat_out=feat_out,
        subsampling=subsampling,
        subsampling_factor=subsampling_factor,
        subsampling_conv_channels=subsampling_conv_channels,
        ff_expansion_factor=ff_expansion_factor,
        self_attention_model=self_attention_model,
        n_heads=n_heads,
        att_context_size=att_context_size,
        xscaling=True,
        untie_biases=True,
        pos_emb_max_len=5000,
        conv_kernel_size=conv_kernel_size,
        conv_norm_type=conv_norm_type,
        dropout=0.1,
        dropout_emb=0.1,
        dropout_att=0.0,
    )
    audio_signal = torch.randn(2, 1600, 80, requires_grad=True)
    x_lens = torch.tensor([1400, 1600])
    y, y_lens = encoder.forward(audio_signal, x_lens)
    y.sum().backward()
