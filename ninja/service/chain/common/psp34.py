ABI = """
{
  "source": {
    "hash": "0x0cdb3ad4165515ea6cf17f000182a80b2e016f3d3a124626ce562a6b6bcc3b01",
    "language": "ink! 4.2.1",
    "compiler": "rustc 1.69.0",
    "build_info": {
      "build_mode": "Release",
      "cargo_contract_version": "3.0.1",
      "rust_toolchain": "stable-aarch64-apple-darwin",
      "wasm_opt_settings": {
        "keep_debug_symbols": false,
        "optimization_passes": "Z"
      }
    }
  },
  "contract": {
    "name": "shiden34",
    "version": "1.0.0",
    "authors": [
      "Astar builder"
    ]
  },
  "spec": {
    "constructors": [
      {
        "args": [
          {
            "label": "id",
            "type": {
              "displayName": [
                "Id"
              ],
              "type": 7
            }
          },
          {
            "label": "imageUrl",
            "type": {
              "displayName": [
                "String"
              ],
              "type": 6
            }
          }
        ],
        "default": false,
        "docs": [
          "A constructor which mints the first token to the owner"
        ],
        "label": "new",
        "payable": false,
        "returnType": {
          "displayName": [
            "ink_primitives",
            "ConstructorResult"
          ],
          "type": 11
        },
        "selector": "0x9bae9d5e"
      }
    ],
    "docs": [],
    "environment": {
      "accountId": {
        "displayName": [
          "AccountId"
        ],
        "type": 0
      },
      "balance": {
        "displayName": [
          "Balance"
        ],
        "type": 5
      },
      "blockNumber": {
        "displayName": [
          "BlockNumber"
        ],
        "type": 4
      },
      "chainExtension": {
        "displayName": [
          "ChainExtension"
        ],
        "type": 27
      },
      "hash": {
        "displayName": [
          "Hash"
        ],
        "type": 26
      },
      "maxEventTopics": 4,
      "timestamp": {
        "displayName": [
          "Timestamp"
        ],
        "type": 9
      }
    },
    "events": [],
    "lang_error": {
      "displayName": [
        "ink",
        "LangError"
      ],
      "type": 12
    },
    "messages": [
      {
        "args": [
          {
            "label": "id",
            "type": {
              "displayName": [
                "psp34metadata_external",
                "GetAttributeInput1"
              ],
              "type": 7
            }
          },
          {
            "label": "key",
            "type": {
              "displayName": [
                "psp34metadata_external",
                "GetAttributeInput2"
              ],
              "type": 6
            }
          }
        ],
        "default": false,
        "docs": [],
        "label": "PSP34Metadata::get_attribute",
        "mutates": false,
        "payable": false,
        "returnType": {
          "displayName": [
            "ink",
            "MessageResult"
          ],
          "type": 13
        },
        "selector": "0xf19d48d1"
      },
      {
        "args": [
          {
            "label": "owner",
            "type": {
              "displayName": [
                "psp34_external",
                "AllowanceInput1"
              ],
              "type": 0
            }
          },
          {
            "label": "operator",
            "type": {
              "displayName": [
                "psp34_external",
                "AllowanceInput2"
              ],
              "type": 0
            }
          },
          {
            "label": "id",
            "type": {
              "displayName": [
                "psp34_external",
                "AllowanceInput3"
              ],
              "type": 15
            }
          }
        ],
        "default": false,
        "docs": [],
        "label": "PSP34::allowance",
        "mutates": false,
        "payable": false,
        "returnType": {
          "displayName": [
            "ink",
            "MessageResult"
          ],
          "type": 16
        },
        "selector": "0x4790f55a"
      },
      {
        "args": [
          {
            "label": "to",
            "type": {
              "displayName": [
                "psp34_external",
                "TransferInput1"
              ],
              "type": 0
            }
          },
          {
            "label": "id",
            "type": {
              "displayName": [
                "psp34_external",
                "TransferInput2"
              ],
              "type": 7
            }
          },
          {
            "label": "data",
            "type": {
              "displayName": [
                "psp34_external",
                "TransferInput3"
              ],
              "type": 10
            }
          }
        ],
        "default": false,
        "docs": [],
        "label": "PSP34::transfer",
        "mutates": true,
        "payable": false,
        "returnType": {
          "displayName": [
            "ink",
            "MessageResult"
          ],
          "type": 18
        },
        "selector": "0x3128d61b"
      },
      {
        "args": [],
        "default": false,
        "docs": [],
        "label": "PSP34::total_supply",
        "mutates": false,
        "payable": false,
        "returnType": {
          "displayName": [
            "ink",
            "MessageResult"
          ],
          "type": 21
        },
        "selector": "0x628413fe"
      },
      {
        "args": [
          {
            "label": "operator",
            "type": {
              "displayName": [
                "psp34_external",
                "ApproveInput1"
              ],
              "type": 0
            }
          },
          {
            "label": "id",
            "type": {
              "displayName": [
                "psp34_external",
                "ApproveInput2"
              ],
              "type": 15
            }
          },
          {
            "label": "approved",
            "type": {
              "displayName": [
                "psp34_external",
                "ApproveInput3"
              ],
              "type": 17
            }
          }
        ],
        "default": false,
        "docs": [],
        "label": "PSP34::approve",
        "mutates": true,
        "payable": false,
        "returnType": {
          "displayName": [
            "ink",
            "MessageResult"
          ],
          "type": 18
        },
        "selector": "0x1932a8b0"
      },
      {
        "args": [
          {
            "label": "owner",
            "type": {
              "displayName": [
                "psp34_external",
                "BalanceOfInput1"
              ],
              "type": 0
            }
          }
        ],
        "default": false,
        "docs": [],
        "label": "PSP34::balance_of",
        "mutates": false,
        "payable": false,
        "returnType": {
          "displayName": [
            "ink",
            "MessageResult"
          ],
          "type": 22
        },
        "selector": "0xcde7e55f"
      },
      {
        "args": [],
        "default": false,
        "docs": [],
        "label": "PSP34::collection_id",
        "mutates": false,
        "payable": false,
        "returnType": {
          "displayName": [
            "ink",
            "MessageResult"
          ],
          "type": 23
        },
        "selector": "0xffa27a5f"
      },
      {
        "args": [
          {
            "label": "id",
            "type": {
              "displayName": [
                "psp34_external",
                "OwnerOfInput1"
              ],
              "type": 7
            }
          }
        ],
        "default": false,
        "docs": [],
        "label": "PSP34::owner_of",
        "mutates": false,
        "payable": false,
        "returnType": {
          "displayName": [
            "ink",
            "MessageResult"
          ],
          "type": 24
        },
        "selector": "0x1168624d"
      },
      {
        "args": [
          {
            "label": "account",
            "type": {
              "displayName": [
                "psp34mintable_external",
                "MintInput1"
              ],
              "type": 0
            }
          },
          {
            "label": "id",
            "type": {
              "displayName": [
                "psp34mintable_external",
                "MintInput2"
              ],
              "type": 7
            }
          }
        ],
        "default": false,
        "docs": [],
        "label": "PSP34Mintable::mint",
        "mutates": true,
        "payable": false,
        "returnType": {
          "displayName": [
            "ink",
            "MessageResult"
          ],
          "type": 18
        },
        "selector": "0x6c41f2ec"
      }
    ]
  },
  "storage": {
    "root": {
      "layout": {
        "struct": {
          "fields": [
            {
              "layout": {
                "struct": {
                  "fields": [
                    {
                      "layout": {
                        "root": {
                          "layout": {
                            "leaf": {
                              "key": "0x252d8eda",
                              "ty": 0
                            }
                          },
                          "root_key": "0x252d8eda"
                        }
                      },
                      "name": "token_owner"
                    },
                    {
                      "layout": {
                        "root": {
                          "layout": {
                            "leaf": {
                              "key": "0xcb1393da",
                              "ty": 3
                            }
                          },
                          "root_key": "0xcb1393da"
                        }
                      },
                      "name": "operator_approvals"
                    },
                    {
                      "layout": {
                        "root": {
                          "layout": {
                            "leaf": {
                              "key": "0xf957bbd8",
                              "ty": 4
                            }
                          },
                          "root_key": "0xf957bbd8"
                        }
                      },
                      "name": "owned_tokens_count"
                    },
                    {
                      "layout": {
                        "root": {
                          "layout": {
                            "leaf": {
                              "key": "0xe3d7d04e",
                              "ty": 5
                            }
                          },
                          "root_key": "0xe3d7d04e"
                        }
                      },
                      "name": "total_supply"
                    }
                  ],
                  "name": "Data"
                }
              },
              "name": "psp34"
            },
            {
              "layout": {
                "struct": {
                  "fields": [
                    {
                      "layout": {
                        "root": {
                          "layout": {
                            "leaf": {
                              "key": "0xdc803caf",
                              "ty": 6
                            }
                          },
                          "root_key": "0xdc803caf"
                        }
                      },
                      "name": "attributes"
                    }
                  ],
                  "name": "Data"
                }
              },
              "name": "metadata"
            }
          ],
          "name": "Contract"
        }
      },
      "root_key": "0x00000000"
    }
  },
  "types": [
    {
      "id": 0,
      "type": {
        "def": {
          "composite": {
            "fields": [
              {
                "type": 1,
                "typeName": "[u8; 32]"
              }
            ]
          }
        },
        "path": [
          "ink_primitives",
          "types",
          "AccountId"
        ]
      }
    },
    {
      "id": 1,
      "type": {
        "def": {
          "array": {
            "len": 32,
            "type": 2
          }
        }
      }
    },
    {
      "id": 2,
      "type": {
        "def": {
          "primitive": "u8"
        }
      }
    },
    {
      "id": 3,
      "type": {
        "def": {
          "tuple": []
        }
      }
    },
    {
      "id": 4,
      "type": {
        "def": {
          "primitive": "u32"
        }
      }
    },
    {
      "id": 5,
      "type": {
        "def": {
          "primitive": "u128"
        }
      }
    },
    {
      "id": 6,
      "type": {
        "def": {
          "primitive": "str"
        }
      }
    },
    {
      "id": 7,
      "type": {
        "def": {
          "variant": {
            "variants": [
              {
                "fields": [
                  {
                    "type": 2,
                    "typeName": "u8"
                  }
                ],
                "index": 0,
                "name": "U8"
              },
              {
                "fields": [
                  {
                    "type": 8,
                    "typeName": "u16"
                  }
                ],
                "index": 1,
                "name": "U16"
              },
              {
                "fields": [
                  {
                    "type": 4,
                    "typeName": "u32"
                  }
                ],
                "index": 2,
                "name": "U32"
              },
              {
                "fields": [
                  {
                    "type": 9,
                    "typeName": "u64"
                  }
                ],
                "index": 3,
                "name": "U64"
              },
              {
                "fields": [
                  {
                    "type": 5,
                    "typeName": "u128"
                  }
                ],
                "index": 4,
                "name": "U128"
              },
              {
                "fields": [
                  {
                    "type": 10,
                    "typeName": "Vec<u8>"
                  }
                ],
                "index": 5,
                "name": "Bytes"
              }
            ]
          }
        },
        "path": [
          "openbrush_contracts",
          "traits",
          "types",
          "Id"
        ]
      }
    },
    {
      "id": 8,
      "type": {
        "def": {
          "primitive": "u16"
        }
      }
    },
    {
      "id": 9,
      "type": {
        "def": {
          "primitive": "u64"
        }
      }
    },
    {
      "id": 10,
      "type": {
        "def": {
          "sequence": {
            "type": 2
          }
        }
      }
    },
    {
      "id": 11,
      "type": {
        "def": {
          "variant": {
            "variants": [
              {
                "fields": [
                  {
                    "type": 3
                  }
                ],
                "index": 0,
                "name": "Ok"
              },
              {
                "fields": [
                  {
                    "type": 12
                  }
                ],
                "index": 1,
                "name": "Err"
              }
            ]
          }
        },
        "params": [
          {
            "name": "T",
            "type": 3
          },
          {
            "name": "E",
            "type": 12
          }
        ],
        "path": [
          "Result"
        ]
      }
    },
    {
      "id": 12,
      "type": {
        "def": {
          "variant": {
            "variants": [
              {
                "index": 1,
                "name": "CouldNotReadInput"
              }
            ]
          }
        },
        "path": [
          "ink_primitives",
          "LangError"
        ]
      }
    },
    {
      "id": 13,
      "type": {
        "def": {
          "variant": {
            "variants": [
              {
                "fields": [
                  {
                    "type": 14
                  }
                ],
                "index": 0,
                "name": "Ok"
              },
              {
                "fields": [
                  {
                    "type": 12
                  }
                ],
                "index": 1,
                "name": "Err"
              }
            ]
          }
        },
        "params": [
          {
            "name": "T",
            "type": 14
          },
          {
            "name": "E",
            "type": 12
          }
        ],
        "path": [
          "Result"
        ]
      }
    },
    {
      "id": 14,
      "type": {
        "def": {
          "variant": {
            "variants": [
              {
                "index": 0,
                "name": "None"
              },
              {
                "fields": [
                  {
                    "type": 6
                  }
                ],
                "index": 1,
                "name": "Some"
              }
            ]
          }
        },
        "params": [
          {
            "name": "T",
            "type": 6
          }
        ],
        "path": [
          "Option"
        ]
      }
    },
    {
      "id": 15,
      "type": {
        "def": {
          "variant": {
            "variants": [
              {
                "index": 0,
                "name": "None"
              },
              {
                "fields": [
                  {
                    "type": 7
                  }
                ],
                "index": 1,
                "name": "Some"
              }
            ]
          }
        },
        "params": [
          {
            "name": "T",
            "type": 7
          }
        ],
        "path": [
          "Option"
        ]
      }
    },
    {
      "id": 16,
      "type": {
        "def": {
          "variant": {
            "variants": [
              {
                "fields": [
                  {
                    "type": 17
                  }
                ],
                "index": 0,
                "name": "Ok"
              },
              {
                "fields": [
                  {
                    "type": 12
                  }
                ],
                "index": 1,
                "name": "Err"
              }
            ]
          }
        },
        "params": [
          {
            "name": "T",
            "type": 17
          },
          {
            "name": "E",
            "type": 12
          }
        ],
        "path": [
          "Result"
        ]
      }
    },
    {
      "id": 17,
      "type": {
        "def": {
          "primitive": "bool"
        }
      }
    },
    {
      "id": 18,
      "type": {
        "def": {
          "variant": {
            "variants": [
              {
                "fields": [
                  {
                    "type": 19
                  }
                ],
                "index": 0,
                "name": "Ok"
              },
              {
                "fields": [
                  {
                    "type": 12
                  }
                ],
                "index": 1,
                "name": "Err"
              }
            ]
          }
        },
        "params": [
          {
            "name": "T",
            "type": 19
          },
          {
            "name": "E",
            "type": 12
          }
        ],
        "path": [
          "Result"
        ]
      }
    },
    {
      "id": 19,
      "type": {
        "def": {
          "variant": {
            "variants": [
              {
                "fields": [
                  {
                    "type": 3
                  }
                ],
                "index": 0,
                "name": "Ok"
              },
              {
                "fields": [
                  {
                    "type": 20
                  }
                ],
                "index": 1,
                "name": "Err"
              }
            ]
          }
        },
        "params": [
          {
            "name": "T",
            "type": 3
          },
          {
            "name": "E",
            "type": 20
          }
        ],
        "path": [
          "Result"
        ]
      }
    },
    {
      "id": 20,
      "type": {
        "def": {
          "variant": {
            "variants": [
              {
                "fields": [
                  {
                    "type": 6,
                    "typeName": "String"
                  }
                ],
                "index": 0,
                "name": "Custom"
              },
              {
                "index": 1,
                "name": "SelfApprove"
              },
              {
                "index": 2,
                "name": "NotApproved"
              },
              {
                "index": 3,
                "name": "TokenExists"
              },
              {
                "index": 4,
                "name": "TokenNotExists"
              },
              {
                "fields": [
                  {
                    "type": 6,
                    "typeName": "String"
                  }
                ],
                "index": 5,
                "name": "SafeTransferCheckFailed"
              }
            ]
          }
        },
        "path": [
          "openbrush_contracts",
          "traits",
          "errors",
          "psp34",
          "PSP34Error"
        ]
      }
    },
    {
      "id": 21,
      "type": {
        "def": {
          "variant": {
            "variants": [
              {
                "fields": [
                  {
                    "type": 5
                  }
                ],
                "index": 0,
                "name": "Ok"
              },
              {
                "fields": [
                  {
                    "type": 12
                  }
                ],
                "index": 1,
                "name": "Err"
              }
            ]
          }
        },
        "params": [
          {
            "name": "T",
            "type": 5
          },
          {
            "name": "E",
            "type": 12
          }
        ],
        "path": [
          "Result"
        ]
      }
    },
    {
      "id": 22,
      "type": {
        "def": {
          "variant": {
            "variants": [
              {
                "fields": [
                  {
                    "type": 4
                  }
                ],
                "index": 0,
                "name": "Ok"
              },
              {
                "fields": [
                  {
                    "type": 12
                  }
                ],
                "index": 1,
                "name": "Err"
              }
            ]
          }
        },
        "params": [
          {
            "name": "T",
            "type": 4
          },
          {
            "name": "E",
            "type": 12
          }
        ],
        "path": [
          "Result"
        ]
      }
    },
    {
      "id": 23,
      "type": {
        "def": {
          "variant": {
            "variants": [
              {
                "fields": [
                  {
                    "type": 7
                  }
                ],
                "index": 0,
                "name": "Ok"
              },
              {
                "fields": [
                  {
                    "type": 12
                  }
                ],
                "index": 1,
                "name": "Err"
              }
            ]
          }
        },
        "params": [
          {
            "name": "T",
            "type": 7
          },
          {
            "name": "E",
            "type": 12
          }
        ],
        "path": [
          "Result"
        ]
      }
    },
    {
      "id": 24,
      "type": {
        "def": {
          "variant": {
            "variants": [
              {
                "fields": [
                  {
                    "type": 25
                  }
                ],
                "index": 0,
                "name": "Ok"
              },
              {
                "fields": [
                  {
                    "type": 12
                  }
                ],
                "index": 1,
                "name": "Err"
              }
            ]
          }
        },
        "params": [
          {
            "name": "T",
            "type": 25
          },
          {
            "name": "E",
            "type": 12
          }
        ],
        "path": [
          "Result"
        ]
      }
    },
    {
      "id": 25,
      "type": {
        "def": {
          "variant": {
            "variants": [
              {
                "index": 0,
                "name": "None"
              },
              {
                "fields": [
                  {
                    "type": 0
                  }
                ],
                "index": 1,
                "name": "Some"
              }
            ]
          }
        },
        "params": [
          {
            "name": "T",
            "type": 0
          }
        ],
        "path": [
          "Option"
        ]
      }
    },
    {
      "id": 26,
      "type": {
        "def": {
          "composite": {
            "fields": [
              {
                "type": 1,
                "typeName": "[u8; 32]"
              }
            ]
          }
        },
        "path": [
          "ink_primitives",
          "types",
          "Hash"
        ]
      }
    },
    {
      "id": 27,
      "type": {
        "def": {
          "variant": {}
        },
        "path": [
          "ink_env",
          "types",
          "NoChainExtension"
        ]
      }
    }
  ],
  "version": "4"
}"""