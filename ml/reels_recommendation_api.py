def get_item_based_recommendations(user_id, user_item_matrix, item_similarity_df, n=5):
    user_ratings = user_item_matrix.loc[user_id]
    weighted_sum = item_similarity_df.dot(user_ratings)
    already_watched = user_ratings[user_ratings > 0].index
    recommendations = weighted_sum.drop(already_watched).sort_values(ascending=False)
    return recommendations.head(n).index.tolist()