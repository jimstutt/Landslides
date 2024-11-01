# After running risk analysis
risk_scores, risk_zones, risk_factors = calculate_landslide_risk(elevation_data)
high_risk_communities = identify_high_risk_communities(risk_scores, population_data)

# Create basic visualizations
visualize_risk_map(risk_scores, risk_zones)
plot_risk_factors(risk_factors)

# Create interactive map
interactive_map = create_interactive_map(risk_scores, 
                                       lat_bounds=(min_lat, max_lat),
                                       lon_bounds=(min_lon, max_lon))

# Generate comprehensive report
report_path = generate_risk_report(risk_scores, risk_zones, 
                                 high_risk_communities, 
                                 output_dir="./reports")

