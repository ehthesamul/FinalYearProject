def summarizer(article):
    from simpletransformers.seq2seq import Seq2SeqModel, Seq2SeqArgs
    model = Seq2SeqModel(
    encoder_decoder_type="bart",
    encoder_decoder_name="outputs_Sum/best_model",use_cuda=False)
    prediction = model.predict(
        [
            article
        ]
    )
    #print(prediction[0])
    return prediction[0]