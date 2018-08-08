const app = new Vue({
  el: "#app",
  data: {
    response: null,
    tokenizer: "standard",
    tokenFilter: [],
    rawTextInput: "SomeFoxes are quick-foxes, others are_not",
    textInput: "SomeFoxes are quick-foxes, others are_not",
    tokenizerConfig: {},
    tokenizers: [
      {
        name: "standard",
        options: [{ name: "max_token_length", default: 255 }]
      },
      { name: "letter", options: [] },
      { name: "lowercase", options: [] },
      {
        name: "whitespace",
        options: [{ name: "max_token_length", default: 255 }]
      },
      {
        name: "uax_url_email",
        options: [{ name: "max_token_length", default: 255 }]
      },
      {
        name: "classic",
        options: [{ name: "max_token_length", default: 255 }]
      },
      {
        name: "ngram",
        options: [
          { name: "min_gram", default: 1 },
          { name: "max_gram", default: 2 },
          { name: "token_chars", default: [] }
        ]
      },
      {
        name: "edge_ngram",
        options: [
          { name: "min_gram", default: 1 },
          { name: "max_gram", default: 2 },
          { name: "token_chars", default: [] }
        ]
      }
      // { name: "keyword", options: [{ name: "buffer_size", default: "256" }] },
      // {
      //   name: "pattern",
      //   options: [
      //     { name: "pattern", default: "W+" },
      //     { name: "flags", default: "" },
      //     { name: "group", default: -1 }
      //   ]
      // }
    ],
    tokenFilters: [
      "standard",
      "asciifolding",
      "flatten_graph",
      "lowercase",
      "uppercase",
      "nGram",
      "edgeNGram",
      "porter_stem",
      "stop",
      "word_delimiter",
      "word_delimiter_graph",
      "shingle",
      "snowball",
      "reverse",
      "kstem"
      // "length",
      // "my_stemmer"
    ]
  },
  mounted() {
    this.doFetch();
  },
  computed: {
    reponseTokens() {
      if (this.response && !this.response.error) {
        return this.response.tokens.map(i => i.token);
      } else {
        return [];
      }
    },
    tokenOptions() {
      return this.tokenizers.find(t => t.name == this.tokenizer).options;
    }
  },
  watch: {
    tokenizer() {
      this.tokenizerConfig = {};
    }
  },
  methods: {
    debouncedTextInput: _.debounce(function() {
      this.textInput = this.rawTextInput;
      this.doFetch();
    }, 300),
    doFetch() {
      // Next tick so watch can reset config before requesting new
      // Otherwise previous config is sent
      this.$nextTick(() => {
        let data = {
          text: this.textInput,
          tokenizer: this.tokenizer,
          tokenConfig: this.tokenizerConfig,
          filters: this.tokenFilter
        };
        $axios.post("", data).then(responseData => {
          this.response = responseData.data;
          this.$nextTick(() => {
            Prism.highlightAll();
          });
        });
      });
    }
  }
});
