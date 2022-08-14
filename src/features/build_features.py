"""Create features"""
# =================
# ==== IMPORTS ====
# =================

import numpy as np
import pandas as pd

from string import punctuation


# ===================
# ==== FUNCTIONS ====
# ===================

def word_count_tweet(df: pd.DataFrame) -> pd.DataFrame:
    """
    """
    df['word_count'] = df.text.apply(lambda x: len(str(x).split()))
    return df


def unique_word_count_tweet(df: pd.DataFrame) -> pd.DataFrame:
    """
    """
    df['unique_word_count'] = df.text.apply(lambda x: len(set(str(x).split())))
    return df


def url_count_tweet(df: pd.DataFrame) -> pd.DataFrame:
    """
    """
    df['url_count'] = df.text.apply(lambda x: len([w for w in str(x).lower().split() if 'http' in w or 'https' in w]))
    return df


def mean_word_length_tweet(df: pd.DataFrame) -> pd.DataFrame:
    """
    """
    df['mean_word_length'] = df.text.apply(lambda x: np.mean([len(w) for w in str(x).split()]))
    return df


def char_count_tweet(df: pd.DataFrame) -> pd.DataFrame:
    """
    """
    df['char_count'] = df.text.apply(lambda x: len(str(x)))
    return df


def punctuation_count_tweet(df: pd.DataFrame) -> pd.DataFrame:
    """
    """
    df['punctuation_count'] = df.text.apply(lambda x: len([c for c in str(x) if c in punctuation]))
    return df


def hashtag_count_tweet(df: pd.DataFrame) -> pd.DataFrame:
    """
    """
    df['hashtag_count'] = df.text.apply(lambda x: len([c for c in str(x) if c == '#']))
    return df


def mention_count_tweet(df: pd.DataFrame) -> pd.DataFrame:
    """
    """
    df['mention_count'] = df.text.apply(lambda x: len([c for c in str(x) if c == '@']))
    return df
