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
            "label": "name",
            "type": {
              "displayName": [
                "String"
              ],
              "type": 8
            }
          },
          {
            "label": "symbol",
            "type": {
              "displayName": [
                "String"
              ],
              "type": 8
            }
          },
          {
            "label": "base_uri",
            "type": {
              "displayName": [
                "String"
              ],
              "type": 8
            }
          }
        ],
        "docs": [],
        "label": "new",
        "payable": false,
        "returnType": {
          "displayName": [
            "ink_primitives",
            "ConstructorResult"
          ],
          "type": 10
        },
        "selector": "0x9bae9d5e"
      }
    ],
    "docs": [],
    "events": [
      {
        "args": [
          {
            "docs": [],
            "indexed": true,
            "label": "from",
            "type": {
              "displayName": [
                "Option"
              ],
              "type": 22
            }
          },
          {
            "docs": [],
            "indexed": true,
            "label": "to",
            "type": {
              "displayName": [
                "Option"
              ],
              "type": 22
            }
          },
          {
            "docs": [],
            "indexed": true,
            "label": "id",
            "type": {
              "displayName": [
                "Id"
              ],
              "type": 17
            }
          }
        ],
        "docs": [
          " Event emitted when a token transfer occurs."
        ],
        "label": "Transfer"
      },
      {
        "args": [
          {
            "docs": [],
            "indexed": true,
            "label": "from",
            "type": {
              "displayName": [
                "AccountId"
              ],
              "type": 0
            }
          },
          {
            "docs": [],
            "indexed": true,
            "label": "to",
            "type": {
              "displayName": [
                "AccountId"
              ],
              "type": 0
            }
          },
          {
            "docs": [],
            "indexed": true,
            "label": "id",
            "type": {
              "displayName": [
                "Option"
              ],
              "type": 19
            }
          },
          {
            "docs": [],
            "indexed": false,
            "label": "approved",
            "type": {
              "displayName": [
                "bool"
              ],
              "type": 9
            }
          }
        ],
        "docs": [
          " Event emitted when a token approve occurs."
        ],
        "label": "Approval"
      }
    ],
    "lang_error": {
      "displayName": [
        "ink",
        "LangError"
      ],
      "type": 11
    },
    "messages": [
      {
        "args": [
          {
            "label": "code_hash",
            "type": {
              "displayName": [],
              "type": 1
            }
          }
        ],
        "docs": [],
        "label": "set_code",
        "mutates": true,
        "payable": false,
        "returnType": {
          "displayName": [
            "ink",
            "MessageResult"
          ],
          "type": 12
        },
        "selector": "0x694fb50f"
      },
      {
        "args": [],
        "docs": [
          " Returns current NFT total supply."
        ],
        "label": "PSP34::total_supply",
        "mutates": false,
        "payable": false,
        "returnType": {
          "displayName": [
            "ink",
            "MessageResult"
          ],
          "type": 15
        },
        "selector": "0x628413fe"
      },
      {
        "args": [],
        "docs": [
          " Returns the collection `Id` of the NFT token.",
          "",
          " This can represents the relationship between tokens/contracts/pallets."
        ],
        "label": "PSP34::collection_id",
        "mutates": false,
        "payable": false,
        "returnType": {
          "displayName": [
            "ink",
            "MessageResult"
          ],
          "type": 16
        },
        "selector": "0xffa27a5f"
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
        "docs": [
          " Returns the balance of the owner.",
          "",
          " This represents the amount of unique tokens the owner has."
        ],
        "label": "PSP34::balance_of",
        "mutates": false,
        "payable": false,
        "returnType": {
          "displayName": [
            "ink",
            "MessageResult"
          ],
          "type": 18
        },
        "selector": "0xcde7e55f"
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
              "type": 19
            }
          }
        ],
        "docs": [
          " Returns `true` if the operator is approved by the owner to withdraw `id` token.",
          " If `id` is `None`, returns `true` if the operator is approved to withdraw all owner's tokens."
        ],
        "label": "PSP34::allowance",
        "mutates": false,
        "payable": false,
        "returnType": {
          "displayName": [
            "ink",
            "MessageResult"
          ],
          "type": 20
        },
        "selector": "0x4790f55a"
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
              "type": 17
            }
          }
        ],
        "docs": [
          " Returns the owner of the token if any."
        ],
        "label": "PSP34::owner_of",
        "mutates": false,
        "payable": false,
        "returnType": {
          "displayName": [
            "ink",
            "MessageResult"
          ],
          "type": 21
        },
        "selector": "0x1168624d"
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
              "type": 19
            }
          },
          {
            "label": "approved",
            "type": {
              "displayName": [
                "psp34_external",
                "ApproveInput3"
              ],
              "type": 9
            }
          }
        ],
        "docs": [
          " Approves `operator` to withdraw the `id` token from the caller's account.",
          " If `id` is `None` approves or disapproves the operator for all tokens of the caller.",
          "",
          " On success a `Approval` event is emitted.",
          "",
          " # Errors",
          "",
          " Returns `SelfApprove` error if it is self approve.",
          "",
          " Returns `NotApproved` error if caller is not owner of `id`."
        ],
        "label": "PSP34::approve",
        "mutates": true,
        "payable": false,
        "returnType": {
          "displayName": [
            "ink",
            "MessageResult"
          ],
          "type": 12
        },
        "selector": "0x1932a8b0"
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
              "type": 17
            }
          },
          {
            "label": "data",
            "type": {
              "displayName": [
                "psp34_external",
                "TransferInput3"
              ],
              "type": 8
            }
          }
        ],
        "docs": [
          " Transfer approved or owned token from caller.",
          "",
          " On success a `Transfer` event is emitted.",
          "",
          " # Errors",
          "",
          " Returns `TokenNotExists` error if `id` does not exist.",
          "",
          " Returns `NotApproved` error if `from` doesn't have allowance for transferring.",
          "",
          " Returns `SafeTransferCheckFailed` error if `to` doesn't accept transfer."
        ],
        "label": "PSP34::transfer",
        "mutates": true,
        "payable": false,
        "returnType": {
          "displayName": [
            "ink",
            "MessageResult"
          ],
          "type": 12
        },
        "selector": "0x3128d61b"
      },
      {
        "args": [
          {
            "label": "owner",
            "type": {
              "displayName": [
                "psp34enumerable_external",
                "OwnersTokenByIndexInput1"
              ],
              "type": 0
            }
          },
          {
            "label": "index",
            "type": {
              "displayName": [
                "psp34enumerable_external",
                "OwnersTokenByIndexInput2"
              ],
              "type": 7
            }
          }
        ],
        "docs": [
          " Returns a token `Id` owned by `owner` at a given `index` of its token list.",
          " Use along with `balance_of` to enumerate all of ``owner``'s tokens.",
          "",
          " The start index is zero."
        ],
        "label": "PSP34Enumerable::owners_token_by_index",
        "mutates": false,
        "payable": false,
        "returnType": {
          "displayName": [
            "ink",
            "MessageResult"
          ],
          "type": 23
        },
        "selector": "0x3bcfb511"
      },
      {
        "args": [
          {
            "label": "index",
            "type": {
              "displayName": [
                "psp34enumerable_external",
                "TokenByIndexInput1"
              ],
              "type": 7
            }
          }
        ],
        "docs": [
          " Returns a token `Id` at a given `index` of all the tokens stored by the contract.",
          " Use along with `total_supply` to enumerate all tokens.",
          "",
          " The start index is zero."
        ],
        "label": "PSP34Enumerable::token_by_index",
        "mutates": false,
        "payable": false,
        "returnType": {
          "displayName": [
            "ink",
            "MessageResult"
          ],
          "type": 23
        },
        "selector": "0xcd0340d0"
      },
      {
        "args": [
          {
            "label": "id",
            "type": {
              "displayName": [
                "psp34metadata_external",
                "GetAttributeInput1"
              ],
              "type": 17
            }
          },
          {
            "label": "key",
            "type": {
              "displayName": [
                "psp34metadata_external",
                "GetAttributeInput2"
              ],
              "type": 8
            }
          }
        ],
        "docs": [
          " Returns the attribute of `id` for the given `key`.",
          "",
          " If `id` is a collection id of the token, it returns attributes for collection."
        ],
        "label": "PSP34Metadata::get_attribute",
        "mutates": false,
        "payable": false,
        "returnType": {
          "displayName": [
            "ink",
            "MessageResult"
          ],
          "type": 25
        },
        "selector": "0xf19d48d1"
      },
      {
        "args": [],
        "docs": [
          " Returns the address of the current owner."
        ],
        "label": "Ownable::owner",
        "mutates": false,
        "payable": false,
        "returnType": {
          "displayName": [
            "ink",
            "MessageResult"
          ],
          "type": 27
        },
        "selector": "0x4fa43c8c"
      },
      {
        "args": [
          {
            "label": "new_owner",
            "type": {
              "displayName": [
                "ownable_external",
                "TransferOwnershipInput1"
              ],
              "type": 0
            }
          }
        ],
        "docs": [
          " Transfers ownership of the contract to a `new_owner`.",
          " Can only be called by the current owner.",
          "",
          " On success a `OwnershipTransferred` event is emitted.",
          "",
          " # Errors",
          "",
          " Panics with `CallerIsNotOwner` error if caller is not owner.",
          "",
          " Panics with `NewOwnerIsZero` error if new owner's address is zero."
        ],
        "label": "Ownable::transfer_ownership",
        "mutates": true,
        "payable": false,
        "returnType": {
          "displayName": [
            "ink",
            "MessageResult"
          ],
          "type": 28
        },
        "selector": "0x11f43efd"
      },
      {
        "args": [],
        "docs": [
          " Leaves the contract without owner. It will not be possible to call",
          " owner's functions anymore. Can only be called by the current owner.",
          "",
          " NOTE: Renouncing ownership will leave the contract without an owner,",
          " thereby removing any functionality that is only available to the owner.",
          "",
          " On success a `OwnershipTransferred` event is emitted.",
          "",
          " # Errors",
          "",
          " Panics with `CallerIsNotOwner` error if caller is not owner"
        ],
        "label": "Ownable::renounce_ownership",
        "mutates": true,
        "payable": false,
        "returnType": {
          "displayName": [
            "ink",
            "MessageResult"
          ],
          "type": 28
        },
        "selector": "0x5e228753"
      },
      {
        "args": [],
        "docs": [
          " Get max number of tokens which could be minted per call"
        ],
        "label": "PayableMint::get_max_mint_amount",
        "mutates": true,
        "payable": false,
        "returnType": {
          "displayName": [
            "ink",
            "MessageResult"
          ],
          "type": 31
        },
        "selector": "0xefb30f46"
      },
      {
        "args": [
          {
            "label": "max_amount",
            "type": {
              "displayName": [
                "payablemint_external",
                "SetMaxMintAmountInput1"
              ],
              "type": 6
            }
          }
        ],
        "docs": [
          " Set max number of tokens which could be minted per call"
        ],
        "label": "PayableMint::set_max_mint_amount",
        "mutates": true,
        "payable": false,
        "returnType": {
          "displayName": [
            "ink",
            "MessageResult"
          ],
          "type": 12
        },
        "selector": "0xad0dc59a"
      },
      {
        "args": [
          {
            "label": "to",
            "type": {
              "displayName": [
                "payablemint_external",
                "MintInput1"
              ],
              "type": 0
            }
          },
          {
            "label": "mint_amount",
            "type": {
              "displayName": [
                "payablemint_external",
                "MintInput2"
              ],
              "type": 6
            }
          }
        ],
        "docs": [
          " Mint one or more tokens"
        ],
        "label": "PayableMint::mint",
        "mutates": true,
        "payable": true,
        "returnType": {
          "displayName": [
            "ink",
            "MessageResult"
          ],
          "type": 12
        },
        "selector": "0x91435162"
      },
      {
        "args": [
          {
            "label": "status",
            "type": {
              "displayName": [
                "payablemint_external",
                "SetMintEndInput1"
              ],
              "type": 9
            }
          }
        ],
        "docs": [],
        "label": "PayableMint::set_mint_end",
        "mutates": true,
        "payable": false,
        "returnType": {
          "displayName": [
            "ink",
            "MessageResult"
          ],
          "type": 12
        },
        "selector": "0x5c2c7cd6"
      },
      {
        "args": [
          {
            "label": "token_id",
            "type": {
              "displayName": [
                "payablemint_external",
                "TokenUriInput1"
              ],
              "type": 6
            }
          }
        ],
        "docs": [
          " Get URI from token ID"
        ],
        "label": "PayableMint::token_uri",
        "mutates": false,
        "payable": false,
        "returnType": {
          "displayName": [
            "ink",
            "MessageResult"
          ],
          "type": 32
        },
        "selector": "0xad9d6966"
      },
      {
        "args": [
          {
            "label": "uri",
            "type": {
              "displayName": [
                "payablemint_external",
                "SetBaseUriInput1"
              ],
              "type": 34
            }
          }
        ],
        "docs": [
          " Set new value for the baseUri"
        ],
        "label": "PayableMint::set_base_uri",
        "mutates": true,
        "payable": false,
        "returnType": {
          "displayName": [
            "ink",
            "MessageResult"
          ],
          "type": 12
        },
        "selector": "0xa089cf22"
      },
      {
        "args": [],
        "docs": [
          " Mint next available token for the caller"
        ],
        "label": "PayableMint::mint_next",
        "mutates": true,
        "payable": true,
        "returnType": {
          "displayName": [
            "ink",
            "MessageResult"
          ],
          "type": 12
        },
        "selector": "0x122435bc"
      },
      {
        "args": [],
        "docs": [
          " Withdraws funds to contract owner"
        ],
        "label": "PayableMint::withdraw",
        "mutates": true,
        "payable": false,
        "returnType": {
          "displayName": [
            "ink",
            "MessageResult"
          ],
          "type": 12
        },
        "selector": "0x0691ffd2"
      },
      {
        "args": [],
        "docs": [],
        "label": "PayableMint::get_mint_end",
        "mutates": false,
        "payable": false,
        "returnType": {
          "displayName": [
            "ink",
            "MessageResult"
          ],
          "type": 20
        },
        "selector": "0x7ba34a74"
      },
      {
        "args": [
          {
            "label": "account_id",
            "type": {
              "displayName": [
                "payablemint_external",
                "GetIsAccountMintedInput1"
              ],
              "type": 0
            }
          }
        ],
        "docs": [],
        "label": "PayableMint::get_is_account_minted",
        "mutates": false,
        "payable": false,
        "returnType": {
          "displayName": [
            "ink",
            "MessageResult"
          ],
          "type": 20
        },
        "selector": "0x79285ec2"
      },
      {
        "args": [],
        "docs": [
          " Get max supply of tokens"
        ],
        "label": "PayableMint::max_supply",
        "mutates": false,
        "payable": false,
        "returnType": {
          "displayName": [
            "ink",
            "MessageResult"
          ],
          "type": 31
        },
        "selector": "0x37fc025f"
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
                              "key": "0x1cc80634",
                              "ty": 0
                            }
                          },
                          "root_key": "0x1cc80634"
                        }
                      },
                      "name": "token_owner"
                    },
                    {
                      "layout": {
                        "root": {
                          "layout": {
                            "leaf": {
                              "key": "0x7e3fae6b",
                              "ty": 3
                            }
                          },
                          "root_key": "0x7e3fae6b"
                        }
                      },
                      "name": "operator_approvals"
                    },
                    {
                      "layout": {
                        "struct": {
                          "fields": [
                            {
                              "layout": {
                                "root": {
                                  "layout": {
                                    "enum": {
                                      "dispatchKey": "0xca32a240",
                                      "name": "Id",
                                      "variants": {
                                        "0": {
                                          "fields": [
                                            {
                                              "layout": {
                                                "leaf": {
                                                  "key": "0xca32a240",
                                                  "ty": 2
                                                }
                                              },
                                              "name": "0"
                                            }
                                          ],
                                          "name": "U8"
                                        },
                                        "1": {
                                          "fields": [
                                            {
                                              "layout": {
                                                "leaf": {
                                                  "key": "0xca32a240",
                                                  "ty": 4
                                                }
                                              },
                                              "name": "0"
                                            }
                                          ],
                                          "name": "U16"
                                        },
                                        "2": {
                                          "fields": [
                                            {
                                              "layout": {
                                                "leaf": {
                                                  "key": "0xca32a240",
                                                  "ty": 5
                                                }
                                              },
                                              "name": "0"
                                            }
                                          ],
                                          "name": "U32"
                                        },
                                        "3": {
                                          "fields": [
                                            {
                                              "layout": {
                                                "leaf": {
                                                  "key": "0xca32a240",
                                                  "ty": 6
                                                }
                                              },
                                              "name": "0"
                                            }
                                          ],
                                          "name": "U64"
                                        },
                                        "4": {
                                          "fields": [
                                            {
                                              "layout": {
                                                "leaf": {
                                                  "key": "0xca32a240",
                                                  "ty": 7
                                                }
                                              },
                                              "name": "0"
                                            }
                                          ],
                                          "name": "U128"
                                        },
                                        "5": {
                                          "fields": [
                                            {
                                              "layout": {
                                                "leaf": {
                                                  "key": "0xca32a240",
                                                  "ty": 8
                                                }
                                              },
                                              "name": "0"
                                            }
                                          ],
                                          "name": "Bytes"
                                        }
                                      }
                                    }
                                  },
                                  "root_key": "0xca32a240"
                                }
                              },
                              "name": "enumerable"
                            },
                            {
                              "layout": {
                                "enum": {
                                  "dispatchKey": "0x00000000",
                                  "name": "Option",
                                  "variants": {
                                    "0": {
                                      "fields": [],
                                      "name": "None"
                                    },
                                    "1": {
                                      "fields": [
                                        {
                                          "layout": {
                                            "leaf": {
                                              "key": "0x00000000",
                                              "ty": 3
                                            }
                                          },
                                          "name": "0"
                                        }
                                      ],
                                      "name": "Some"
                                    }
                                  }
                                }
                              },
                              "name": "_reserved"
                            }
                          ],
                          "name": "Balances"
                        }
                      },
                      "name": "balances"
                    },
                    {
                      "layout": {
                        "enum": {
                          "dispatchKey": "0x00000000",
                          "name": "Option",
                          "variants": {
                            "0": {
                              "fields": [],
                              "name": "None"
                            },
                            "1": {
                              "fields": [
                                {
                                  "layout": {
                                    "leaf": {
                                      "key": "0x00000000",
                                      "ty": 3
                                    }
                                  },
                                  "name": "0"
                                }
                              ],
                              "name": "Some"
                            }
                          }
                        }
                      },
                      "name": "_reserved"
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
                        "leaf": {
                          "key": "0x00000000",
                          "ty": 2
                        }
                      },
                      "name": "status"
                    },
                    {
                      "layout": {
                        "enum": {
                          "dispatchKey": "0x00000000",
                          "name": "Option",
                          "variants": {
                            "0": {
                              "fields": [],
                              "name": "None"
                            },
                            "1": {
                              "fields": [
                                {
                                  "layout": {
                                    "leaf": {
                                      "key": "0x00000000",
                                      "ty": 3
                                    }
                                  },
                                  "name": "0"
                                }
                              ],
                              "name": "Some"
                            }
                          }
                        }
                      },
                      "name": "_reserved"
                    }
                  ],
                  "name": "Data"
                }
              },
              "name": "guard"
            },
            {
              "layout": {
                "struct": {
                  "fields": [
                    {
                      "layout": {
                        "leaf": {
                          "key": "0x00000000",
                          "ty": 0
                        }
                      },
                      "name": "owner"
                    },
                    {
                      "layout": {
                        "enum": {
                          "dispatchKey": "0x00000000",
                          "name": "Option",
                          "variants": {
                            "0": {
                              "fields": [],
                              "name": "None"
                            },
                            "1": {
                              "fields": [
                                {
                                  "layout": {
                                    "leaf": {
                                      "key": "0x00000000",
                                      "ty": 3
                                    }
                                  },
                                  "name": "0"
                                }
                              ],
                              "name": "Some"
                            }
                          }
                        }
                      },
                      "name": "_reserved"
                    }
                  ],
                  "name": "Data"
                }
              },
              "name": "ownable"
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
                              "key": "0x9b2d2382",
                              "ty": 8
                            }
                          },
                          "root_key": "0x9b2d2382"
                        }
                      },
                      "name": "attributes"
                    },
                    {
                      "layout": {
                        "enum": {
                          "dispatchKey": "0x00000000",
                          "name": "Option",
                          "variants": {
                            "0": {
                              "fields": [],
                              "name": "None"
                            },
                            "1": {
                              "fields": [
                                {
                                  "layout": {
                                    "leaf": {
                                      "key": "0x00000000",
                                      "ty": 3
                                    }
                                  },
                                  "name": "0"
                                }
                              ],
                              "name": "Some"
                            }
                          }
                        }
                      },
                      "name": "_reserved"
                    }
                  ],
                  "name": "Data"
                }
              },
              "name": "metadata"
            },
            {
              "layout": {
                "struct": {
                  "fields": [
                    {
                      "layout": {
                        "leaf": {
                          "key": "0x00000000",
                          "ty": 6
                        }
                      },
                      "name": "last_token_id"
                    },
                    {
                      "layout": {
                        "leaf": {
                          "key": "0x00000000",
                          "ty": 5
                        }
                      },
                      "name": "collection_id"
                    },
                    {
                      "layout": {
                        "leaf": {
                          "key": "0x00000000",
                          "ty": 6
                        }
                      },
                      "name": "max_amount"
                    },
                    {
                      "layout": {
                        "root": {
                          "layout": {
                            "leaf": {
                              "key": "0xb65a7091",
                              "ty": 9
                            }
                          },
                          "root_key": "0xb65a7091"
                        }
                      },
                      "name": "account_minted"
                    },
                    {
                      "layout": {
                        "leaf": {
                          "key": "0x00000000",
                          "ty": 9
                        }
                      },
                      "name": "mint_end"
                    }
                  ],
                  "name": "Data"
                }
              },
              "name": "payable_mint"
            }
          ],
          "name": "Shiden34Contract"
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
          "primitive": "u16"
        }
      }
    },
    {
      "id": 5,
      "type": {
        "def": {
          "primitive": "u32"
        }
      }
    },
    {
      "id": 6,
      "type": {
        "def": {
          "primitive": "u64"
        }
      }
    },
    {
      "id": 7,
      "type": {
        "def": {
          "primitive": "u128"
        }
      }
    },
    {
      "id": 8,
      "type": {
        "def": {
          "sequence": {
            "type": 2
          }
        }
      }
    },
    {
      "id": 9,
      "type": {
        "def": {
          "primitive": "bool"
        }
      }
    },
    {
      "id": 10,
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
                    "type": 11
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
            "type": 11
          }
        ],
        "path": [
          "Result"
        ]
      }
    },
    {
      "id": 11,
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
      "id": 12,
      "type": {
        "def": {
          "variant": {
            "variants": [
              {
                "fields": [
                  {
                    "type": 13
                  }
                ],
                "index": 0,
                "name": "Ok"
              },
              {
                "fields": [
                  {
                    "type": 11
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
            "type": 13
          },
          {
            "name": "E",
            "type": 11
          }
        ],
        "path": [
          "Result"
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
                    "type": 3
                  }
                ],
                "index": 0,
                "name": "Ok"
              },
              {
                "fields": [
                  {
                    "type": 14
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
            "type": 14
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
                "fields": [
                  {
                    "type": 8,
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
                    "type": 8,
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
      "id": 15,
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
                    "type": 11
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
            "type": 11
          }
        ],
        "path": [
          "Result"
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
                    "type": 11
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
            "type": 11
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
                    "type": 4,
                    "typeName": "u16"
                  }
                ],
                "index": 1,
                "name": "U16"
              },
              {
                "fields": [
                  {
                    "type": 5,
                    "typeName": "u32"
                  }
                ],
                "index": 2,
                "name": "U32"
              },
              {
                "fields": [
                  {
                    "type": 6,
                    "typeName": "u64"
                  }
                ],
                "index": 3,
                "name": "U64"
              },
              {
                "fields": [
                  {
                    "type": 7,
                    "typeName": "u128"
                  }
                ],
                "index": 4,
                "name": "U128"
              },
              {
                "fields": [
                  {
                    "type": 8,
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
      "id": 18,
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
                    "type": 11
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
            "type": 11
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
                "index": 0,
                "name": "None"
              },
              {
                "fields": [
                  {
                    "type": 17
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
            "type": 17
          }
        ],
        "path": [
          "Option"
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
                    "type": 9
                  }
                ],
                "index": 0,
                "name": "Ok"
              },
              {
                "fields": [
                  {
                    "type": 11
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
            "type": 9
          },
          {
            "name": "E",
            "type": 11
          }
        ],
        "path": [
          "Result"
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
                    "type": 22
                  }
                ],
                "index": 0,
                "name": "Ok"
              },
              {
                "fields": [
                  {
                    "type": 11
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
            "type": 22
          },
          {
            "name": "E",
            "type": 11
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
      "id": 23,
      "type": {
        "def": {
          "variant": {
            "variants": [
              {
                "fields": [
                  {
                    "type": 24
                  }
                ],
                "index": 0,
                "name": "Ok"
              },
              {
                "fields": [
                  {
                    "type": 11
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
            "type": 24
          },
          {
            "name": "E",
            "type": 11
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
                    "type": 17
                  }
                ],
                "index": 0,
                "name": "Ok"
              },
              {
                "fields": [
                  {
                    "type": 14
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
            "type": 14
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
                "fields": [
                  {
                    "type": 26
                  }
                ],
                "index": 0,
                "name": "Ok"
              },
              {
                "fields": [
                  {
                    "type": 11
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
            "type": 26
          },
          {
            "name": "E",
            "type": 11
          }
        ],
        "path": [
          "Result"
        ]
      }
    },
    {
      "id": 26,
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
                    "type": 8
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
            "type": 8
          }
        ],
        "path": [
          "Option"
        ]
      }
    },
    {
      "id": 27,
      "type": {
        "def": {
          "variant": {
            "variants": [
              {
                "fields": [
                  {
                    "type": 0
                  }
                ],
                "index": 0,
                "name": "Ok"
              },
              {
                "fields": [
                  {
                    "type": 11
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
            "type": 0
          },
          {
            "name": "E",
            "type": 11
          }
        ],
        "path": [
          "Result"
        ]
      }
    },
    {
      "id": 28,
      "type": {
        "def": {
          "variant": {
            "variants": [
              {
                "fields": [
                  {
                    "type": 29
                  }
                ],
                "index": 0,
                "name": "Ok"
              },
              {
                "fields": [
                  {
                    "type": 11
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
            "type": 29
          },
          {
            "name": "E",
            "type": 11
          }
        ],
        "path": [
          "Result"
        ]
      }
    },
    {
      "id": 29,
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
                    "type": 30
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
            "type": 30
          }
        ],
        "path": [
          "Result"
        ]
      }
    },
    {
      "id": 30,
      "type": {
        "def": {
          "variant": {
            "variants": [
              {
                "index": 0,
                "name": "CallerIsNotOwner"
              },
              {
                "index": 1,
                "name": "NewOwnerIsZero"
              }
            ]
          }
        },
        "path": [
          "openbrush_contracts",
          "traits",
          "errors",
          "ownable",
          "OwnableError"
        ]
      }
    },
    {
      "id": 31,
      "type": {
        "def": {
          "variant": {
            "variants": [
              {
                "fields": [
                  {
                    "type": 6
                  }
                ],
                "index": 0,
                "name": "Ok"
              },
              {
                "fields": [
                  {
                    "type": 11
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
            "type": 6
          },
          {
            "name": "E",
            "type": 11
          }
        ],
        "path": [
          "Result"
        ]
      }
    },
    {
      "id": 32,
      "type": {
        "def": {
          "variant": {
            "variants": [
              {
                "fields": [
                  {
                    "type": 33
                  }
                ],
                "index": 0,
                "name": "Ok"
              },
              {
                "fields": [
                  {
                    "type": 11
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
            "type": 33
          },
          {
            "name": "E",
            "type": 11
          }
        ],
        "path": [
          "Result"
        ]
      }
    },
    {
      "id": 33,
      "type": {
        "def": {
          "variant": {
            "variants": [
              {
                "fields": [
                  {
                    "type": 34
                  }
                ],
                "index": 0,
                "name": "Ok"
              },
              {
                "fields": [
                  {
                    "type": 14
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
            "type": 34
          },
          {
            "name": "E",
            "type": 14
          }
        ],
        "path": [
          "Result"
        ]
      }
    },
    {
      "id": 34,
      "type": {
        "def": {
          "primitive": "str"
        }
      }
    }
  ],
  "version": "4"
}"""