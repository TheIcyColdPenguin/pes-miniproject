<script lang="ts">
	import { fields, laptops, searchCheckboxes, searchRanges, searchWords } from '../stores/results';
	import { onMount } from 'svelte';
	import type { Ranges } from '../types/types';
	import { getLaptops } from '../util/search';

	onMount(async () => {
		const res = await fetch('http://localhost:8000/filters');
		if (!res.ok) {
			return;
		}
		$fields = await res.json();
	});

	$: {
		if (!Object.keys($searchCheckboxes).length) {
			for (const checkbox in $fields.checkboxes) {
				$searchCheckboxes[checkbox] = [];
			}
		}
		if (!Object.keys($searchRanges).length) {
			for (const range in $fields.ranges) {
				$searchRanges[range] = [...$fields.ranges[range as keyof Ranges]];
			}
		}
		(async () => {
			$laptops = await getLaptops($searchCheckboxes, $searchRanges, $searchWords);
		})();
	}

	function capitalise(str: string) {
		str = str.replace('os', 'OS').replace('res', 'resolution').replace('diag', 'diagonal');
		return str[0].toUpperCase() + str.slice(1).replace(/_/g, ' ');
	}
</script>

<main>
	<form>
		{#each Object.entries($fields.checkboxes) as [checkbox, values] (checkbox)}
			<fieldset>
				<h4>{capitalise(checkbox)}</h4>
				{#each values as value}
					<label>
						<input
							type="checkbox"
							name={checkbox}
							bind:group={$searchCheckboxes[checkbox]}
							{value}
						/>
						{value}
					</label>
				{/each}
			</fieldset>
		{/each}
		{#each Object.entries($fields.ranges) as [range, [start, end]] (range)}
			<fieldset>
				<h4>{capitalise(range)}: {$searchRanges[range][0]}-{$searchRanges[range][1]}</h4>
				<input
					class="from-slider"
					name={range}
					type="range"
					bind:value={$searchRanges[range][0]}
					min={start}
					max={$searchRanges[range][1]}
				/>
				<input
					class="to-slider"
					name={range}
					type="range"
					bind:value={$searchRanges[range][1]}
					min={$searchRanges[range][0]}
					max={end}
				/>
			</fieldset>
		{/each}
	</form>
</main>

<style>
	main {
		overflow-y: scroll;
	}

	label {
		display: block;
	}

	fieldset {
		background-color: #ffffff77;
		border-radius: 5px;
		border: none;
		margin: 0.5rem;
	}
</style>
