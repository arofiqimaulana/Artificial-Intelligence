# untuk mengetahui index mapping
GET merek/_mapping

# untuk mengetahui perhitungan hasil salah satu dokumen
GET merek/_explain/43912344
{
  "query": {
    "bool": {
      "must": [
        {
          "more_like_this": {
            "fields": ["nama_merek"],
            "like": "alena the label",
            "min_term_freq": 1,
            "boost": 4
          }
        }
      ]
    }
  }
}

# TES 1
GET merek/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "dis_max": {
            "tie_breaker": 0.3,
            "queries": [
              {
                "match": {
                  "nama_merek": {
                  "query": "alena the label",
                  "fuzziness": "AUTO",
                  "operator": "AND",
                  "boost": 5
                  }
                }
              },
              {
                "more_like_this": {
                  "fields": ["nama_merek"],
                  "like": "alena the label",
                  "min_term_freq": 1,
                  "boost": 4
                }
              },
              {
                "match": {
                  "nama_merek": {
                    "query": "alena the label",
                    "fuzziness": "AUTO",
                    "operator": "OR", 
                    "boost": 3
                  }
                }
              }
            ]
          }
        }
      ]
    }
  },
  "_source": ["id", "nomor_permohonan", "nama_merek"],
  "from": 0,
  "size": 30,
  "explain": true
}

# TES 2
GET merek/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "bool": {
            "should": [
              {
                "match": {
                  "nama_merek": {
                  "query": "Alèna the label",
                  "fuzziness": "AUTO",
                  "operator": "AND",
                  "boost": 5
                  }
                }
              },
              {
                "match": {
                  "nama_merek": {
                    "query": "Alèna the label", 
                    "fuzziness": "AUTO",
                    "operator": "OR", 
                    "boost": 3
                  }
                }
              }
            ]
          }
        }
      ]
    }
  },
  "_source": [
    "id",
    "nomor_permohonan",
    "nama_merek"
  ],
  "from": 0,
  "size": 30
}

# TES 3
GET merek/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "bool": {
            "should": [
              {
                "match": {
                  "nama_merek": {
                  "query": "giantree",
                  "fuzziness": "AUTO", 
                  "operator": "AND",
                  "boost": 5
                  }
                }
              },
              {
                "match": {
                  "nama_merek": {
                    "query": "giantree",
                    "operator": "OR",
                    "boost": 3
                  }
                }
              },
              {
                "match": {
                  "nama_merek": {
                    "query": "giantree",
                    "operator": "OR",
                    "boost": 1
                  }
                }
              }
            ]
          }
        }
      ]
    }
  },
  "_source": ["id", "nomor_permohonan", "nama_merek"],
  "from": 0,
  "size": 100
}
