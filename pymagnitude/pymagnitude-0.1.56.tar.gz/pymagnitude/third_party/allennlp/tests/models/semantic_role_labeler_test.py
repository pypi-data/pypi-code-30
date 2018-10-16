# pylint: disable=no-self-use,invalid-name



from __future__ import with_statement
from __future__ import division
from __future__ import absolute_import
import subprocess
import os

from flaky import flaky
import pytest
import numpy

from allennlp.common.testing import ModelTestCase
from allennlp.common.params import Params
from allennlp.common.checks import ConfigurationError
from allennlp.models.semantic_role_labeler import convert_bio_tags_to_conll_format
from allennlp.models import Model
from allennlp.models.semantic_role_labeler import write_to_conll_eval_file
from allennlp.nn.util import get_lengths_from_binary_sequence_mask

from io import open
try:
    from itertools import izip
except:
    izip = zip


class SemanticRoleLabelerTest(ModelTestCase):
    def setUp(self):
        super(SemanticRoleLabelerTest, self).setUp()
        self.set_up_model(self.FIXTURES_ROOT / u'srl' / u'experiment.json',
                          self.FIXTURES_ROOT / u'conll_2012')

    def test_srl_model_can_train_save_and_load(self):
        self.ensure_model_can_train_save_and_load(self.param_file)

    @flaky
    def test_batch_predictions_are_consistent(self):
        self.ensure_batch_predictions_are_consistent()

    def test_forward_pass_runs_correctly(self):
        training_tensors = self.dataset.as_tensor_dict()
        output_dict = self.model(**training_tensors)
        class_probs = output_dict[u'class_probabilities'][0].data.numpy()
        numpy.testing.assert_almost_equal(numpy.sum(class_probs, -1),
                                          numpy.ones(class_probs.shape[0]),
                                          decimal=6)

    def test_decode_runs_correctly(self):
        training_tensors = self.dataset.as_tensor_dict()
        output_dict = self.model(**training_tensors)
        decode_output_dict = self.model.decode(output_dict)
        lengths = get_lengths_from_binary_sequence_mask(decode_output_dict[u"mask"]).data.tolist()
        # Hard to check anything concrete which we haven't checked in the above
        # test, so we'll just check that the tags are equal to the lengths
        # of the individual instances, rather than the max length.
        for prediction, length in izip(decode_output_dict[u"tags"], lengths):
            assert len(prediction) == length


    def test_bio_tags_correctly_convert_to_conll_format(self):
        bio_tags = [u"B-ARG-1", u"I-ARG-1", u"O", u"B-V", u"B-ARGM-ADJ", u"O"]
        conll_tags = convert_bio_tags_to_conll_format(bio_tags)
        assert conll_tags == [u"(ARG-1*", u"*)", u"*", u"(V*)", u"(ARGM-ADJ*)", u"*"]

    def test_perl_eval_script_can_run_on_printed_conll_files(self):
        bio_tags = [u"B-ARG-1", u"I-ARG-1", u"O", u"B-V", u"B-ARGM-ADJ", u"O"]
        sentence = [u"Mark", u"and", u"Matt", u"were", u"running", u"fast", u"."]

        gold_file_path = os.path.join(self.TEST_DIR, u"gold_conll_eval.txt")
        prediction_file_path = os.path.join(self.TEST_DIR, u"prediction_conll_eval.txt")
        with open(gold_file_path, u"a+") as gold_file, open(prediction_file_path, u"a+") as prediction_file:
            # Use the same bio tags as prediction vs gold to make it obvious by looking
            # at the perl script output if something is wrong. Write them twice to
            # ensure that the perl script deals with multiple sentences.
            write_to_conll_eval_file(gold_file, prediction_file, 4, sentence, bio_tags, bio_tags)
            write_to_conll_eval_file(gold_file, prediction_file, 4, sentence, bio_tags, bio_tags)

        perl_script_command = [u"perl", unicode(self.TOOLS_ROOT / u"srl-eval.pl"), prediction_file_path, gold_file_path]
        exit_code = subprocess.check_call(perl_script_command)
        assert exit_code == 0

    def test_mismatching_dimensions_throws_configuration_error(self):
        params = Params.from_file(self.param_file)
        # Make the phrase layer wrong - it should be 150 to match
        # the embedding + binary feature dimensions.
        params[u"model"][u"encoder"][u"input_size"] = 10
        with pytest.raises(ConfigurationError):
            Model.from_params(vocab=self.vocab, params=params.pop(u"model"))
