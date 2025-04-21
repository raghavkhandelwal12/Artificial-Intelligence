# Large Language Model(LLM) - Token-Level Processing

`User Input Text` : 

- `Example` : "Hello, how are you?"

`Tokenization` : Breaks inputs into tokens : [15496, 11, 703, 389]

`Embedding Layer` : Tokens converted to dense vectors(semantic meaning).

`Transformer Architecture` : Self-Attention + Feed Forward Layers(Multiple Stacked Blocks).

`Prediction Head` : Softmax over vocabulary -> Predict next token ID.

`Append Predicted Token` : Add predicted token to input sequence.

`Repeat Loop` : Until end condition is met(stop token or max length).

`Detokenization` ;  Convert token IDs back to human-readable text.
